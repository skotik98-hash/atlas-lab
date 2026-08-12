import argparse
import asyncio
import json
from pathlib import Path

from activity_store import log_event
from atlas_status import get_atlas_status
from notifier import send_notification


STATE_PATH = Path(__file__).with_name("data") / "watcher_state.json"


def load_previous_state():
    if not STATE_PATH.exists():
        return None

    try:
        return json.loads(
            STATE_PATH.read_text(encoding="utf-8")
        )
    except Exception:
        return None


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

    STATE_PATH.write_text(
        json.dumps(
            state,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def snapshot():
    data = get_atlas_status()

    return {
        "commit_hash": data["commit_hash"],
        "commit_message": data["commit_message"],
        "working_tree_clean": data["working_tree_clean"],
        "ahead": data["ahead"],
        "behind": data["behind"],
        "pending": data["pending"],
    }


async def record_and_notify(
    event_type,
    notification_type,
    title,
    message,
    metadata=None,
):
    log_event(
        event_type=event_type,
        source="Atlas Watcher",
        title=title,
        details=message,
        metadata=metadata or {},
    )

    await send_notification(
        notification_type,
        title,
        message,
    )


async def process_changes(previous, current):
    # Новый commit
    if previous["commit_hash"] != current["commit_hash"]:
        await record_and_notify(
            "GIT_COMMIT",
            "success",
            "Новый commit в Atlas Lab",
            (
                f"{current['commit_hash']} · "
                f"{current['commit_message']}"
            ),
            {
                "commit_hash": current["commit_hash"],
                "commit_message": current["commit_message"],
            },
        )

    # Рабочее дерево
    if (
        previous["working_tree_clean"]
        != current["working_tree_clean"]
    ):
        if current["working_tree_clean"]:
            await record_and_notify(
                "GIT_CLEAN",
                "success",
                "Рабочее дерево очищено",
                (
                    "Git working tree снова чист. "
                    "Локальных незакоммиченных изменений нет."
                ),
            )
        else:
            await record_and_notify(
                "GIT_DIRTY",
                "warning",
                "В Atlas есть локальные изменения",
                (
                    "Git working tree больше не чист. "
                    "Обнаружены незакоммиченные изменения."
                ),
            )

    # Git Sync
    old_sync = (
        previous["ahead"] == 0
        and previous["behind"] == 0
    )

    new_sync = (
        current["ahead"] == 0
        and current["behind"] == 0
    )

    if old_sync != new_sync:
        if new_sync:
            await record_and_notify(
                "GIT_SYNC_RESTORED",
                "success",
                "Git синхронизация восстановлена",
                "main и origin/main снова синхронизированы.",
            )
        else:
            await record_and_notify(
                "GIT_SYNC_REQUIRED",
                "warning",
                "Git требует синхронизации",
                (
                    f"Ahead: {current['ahead']} · "
                    f"Behind: {current['behind']}"
                ),
                {
                    "ahead": current["ahead"],
                    "behind": current["behind"],
                },
            )

    # Pending Approvals
    if current["pending"] > previous["pending"]:
        difference = (
            current["pending"]
            - previous["pending"]
        )

        await record_and_notify(
            "APPROVAL_PENDING",
            "approval",
            "Появилось новое решение",
            (
                f"Новых запросов: {difference}. "
                f"Всего ожидают решения: {current['pending']}.\n\n"
                "Открой /pending в Atlas Control."
            ),
            {
                "new_pending": difference,
                "total_pending": current["pending"],
            },
        )

    elif (
        current["pending"] < previous["pending"]
        and current["pending"] == 0
    ):
        await record_and_notify(
            "APPROVAL_CLEARED",
            "success",
            "Approval Inbox обработан",
            "Активных запросов на решение больше нет.",
        )


async def run_once():
    current = snapshot()
    previous = load_previous_state()

    if previous is None:
        save_state(current)

        print("✅ Atlas Watcher baseline создан")
        print("🔕 Первичный запуск — уведомления не отправлены")
        return

    await process_changes(previous, current)
    save_state(current)

    print("✅ Atlas Watcher проверил состояние")


async def run_forever(interval):
    print("")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("👁 ATLAS WATCHER · ACTIVE")
    print(f"⏱ Интервал проверки · {interval} сек.")
    print("🧠 Activity Store · CONNECTED")
    print("🔕 Повторные состояния · НЕ ДУБЛИРУЮТСЯ")
    print("⏹ Для остановки: Control + C")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("")

    while True:
        try:
            await run_once()
        except Exception as exc:
            print(
                "⚠️ Ошибка Watcher:",
                type(exc).__name__,
            )

        await asyncio.sleep(interval)


async def main():
    parser = argparse.ArgumentParser(
        description="Atlas State Watcher"
    )

    parser.add_argument(
        "--once",
        action="store_true",
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=15,
    )

    args = parser.parse_args()

    if args.once:
        await run_once()
    else:
        await run_forever(
            max(args.interval, 5)
        )


if __name__ == "__main__":
    asyncio.run(main())

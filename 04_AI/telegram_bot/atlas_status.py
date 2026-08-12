import subprocess
from pathlib import Path

from approval_store import count_approvals


REPO_ROOT = Path(__file__).resolve().parents[2]


def git(*args):
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=5,
    )

    if result.returncode != 0:
        return None

    return result.stdout.strip()


def get_atlas_status():
    branch = git("branch", "--show-current") or "UNKNOWN"

    latest_commit = git(
        "log",
        "-1",
        "--pretty=format:%h|%s",
    )

    if latest_commit and "|" in latest_commit:
        commit_hash, commit_message = latest_commit.split("|", 1)
    else:
        commit_hash = "UNKNOWN"
        commit_message = "Недоступно"

    working_tree = git("status", "--porcelain")

    is_clean = working_tree == ""

    sync = git(
        "rev-list",
        "--left-right",
        "--count",
        "origin/main...main",
    )

    behind = 0
    ahead = 0

    if sync:
        try:
            left, right = sync.split()
            behind = int(left)
            ahead = int(right)
        except Exception:
            pass

    approvals = count_approvals()

    return {
        "branch": branch,
        "commit_hash": commit_hash,
        "commit_message": commit_message,
        "working_tree_clean": is_clean,
        "ahead": ahead,
        "behind": behind,
        "pending": approvals["PENDING"],
        "approved": approvals["APPROVED"],
        "rejected": approvals["REJECTED"],
    }


if __name__ == "__main__":
    data = get_atlas_status()

    print("=== ATLAS REAL STATUS ===")
    print("Branch:", data["branch"])
    print(
        "Working tree:",
        "CLEAN" if data["working_tree_clean"] else "CHANGED",
    )
    print("Ahead:", data["ahead"])
    print("Behind:", data["behind"])
    print(
        "Latest commit:",
        data["commit_hash"],
        data["commit_message"],
    )
    print("Pending approvals:", data["pending"])
    print("Approved:", data["approved"])
    print("Rejected:", data["rejected"])

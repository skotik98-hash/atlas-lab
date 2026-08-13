from contextlib import contextmanager


@contextmanager
def managed_connection(db):
    """Commit/rollback like sqlite3.Connection.__exit__, then always close.

    `with sqlite3.connect(...) as db` does not close the connection.
    """
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    else:
        db.commit()
    finally:
        db.close()

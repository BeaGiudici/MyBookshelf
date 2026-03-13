from src.database.connection import get_session
from src.database.models import Status


def get_all_statuses():
    """Get all statuses from the database"""
    with get_session() as db:
        return db.query(Status).order_by(Status.id).all()


def get_status_by_id(status_id: int):
    """Get a status by its ID"""
    with get_session() as db:
        return db.query(Status).filter(Status.id == status_id).first()


def get_status_by_name(status_name: str):
    """Get a status by its name"""
    with get_session() as db:
        return db.query(Status).filter(Status.name == status_name).first()


def update_status(status: Status):
    """Update a status entry in the database"""
    with get_session() as db:
        db_status = db.merge(status)
        db.commit()
        db.refresh(db_status)
        return db_status


def add_status(status: Status):
    """Add a new status entry to the database"""
    with get_session() as db:
        db.add(status)
        db.commit()
        db.refresh(status)
        return status


def delete_status(status_id: int):
    """Delete a status entry from the database"""
    with get_session() as db:
        db.query(Status).filter(Status.id == status_id).delete()
        db.commit()
        return {"message": f"Status {status_id} deleted successfully"}


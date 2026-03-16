from sqlmodel import Session
from src.database.models import Status


def get_all_statuses(session: Session):
    """Get all statuses from the database"""
    return session.query(Status).order_by(Status.id).all()


def get_status_by_id(session: Session, status_id: int):
    """Get a status by its ID"""
    return session.query(Status).filter(Status.id == status_id).first()


def get_status_by_name(session: Session, status_name: str):
    """Get a status by its name"""
    return session.query(Status).filter(Status.name == status_name).first()


def update_status(session: Session, status: Status):
    """Update a status entry in the database"""
    db_status = session.merge(status)
    session.commit()
    session.refresh(db_status)
    return db_status


def add_status(session: Session, status: Status):
    """Add a new status entry to the database"""
    session.add(status)
    session.commit()
    session.refresh(status)
    return status


def delete_status(session: Session, status_id: int):
    """Delete a status entry from the database"""
    session.query(Status).filter(Status.id == status_id).delete()
    session.commit()
    return {"message": f"Status {status_id} deleted successfully"}

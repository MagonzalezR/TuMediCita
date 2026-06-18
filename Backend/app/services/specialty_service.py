from sqlalchemy.orm import Session

from app.models.specialty import Especialidad


class SpecialtyService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Especialidad).order_by(Especialidad.id).all()

    @staticmethod
    def create(db: Session, payload: dict):
        specialty = Especialidad(**payload)
        db.add(specialty)
        db.commit()
        db.refresh(specialty)
        return specialty

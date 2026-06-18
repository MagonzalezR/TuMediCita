from sqlalchemy.orm import Session

from app.models.doctor import Doctor


class DoctorService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Doctor).order_by(Doctor.id).all()

    @staticmethod
    def get_by_id(db: Session, doctor_id: int):
        return db.query(Doctor).filter(Doctor.id == doctor_id).first()

    @staticmethod
    def create(db: Session, payload: dict):
        doctor = Doctor(**payload)
        db.add(doctor)
        db.commit()
        db.refresh(doctor)
        return doctor

    @staticmethod
    def update(db: Session, doctor: Doctor, payload: dict):
        for key, value in payload.items():
            setattr(doctor, key, value)
        db.commit()
        db.refresh(doctor)
        return doctor

    @staticmethod
    def delete(db: Session, doctor: Doctor):
        db.delete(doctor)
        db.commit()

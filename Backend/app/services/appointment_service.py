from sqlalchemy.orm import Session

from app.models.appointment import Cita


class AppointmentService:
    @staticmethod
    def get_all(db: Session, doctor_id: int | None = None):
        query = db.query(Cita)
        if doctor_id is not None:
            query = query.filter(Cita.doctor_id == doctor_id)
        return query.order_by(Cita.id).all()

    @staticmethod
    def get_by_id(db: Session, appointment_id: int):
        return db.query(Cita).filter(Cita.id == appointment_id).first()

    @staticmethod
    def create(db: Session, payload: dict):
        appointment = Cita(**payload)
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        return appointment

    @staticmethod
    def delete(db: Session, appointment: Cita):
        db.delete(appointment)
        db.commit()

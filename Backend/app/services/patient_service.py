from sqlalchemy.orm import Session

from app.models.patient import Paciente


class PatientService:
    @staticmethod
    def get_all(db: Session):
        return db.query(Paciente).order_by(Paciente.id).all()

    @staticmethod
    def get_by_id(db: Session, patient_id: int):
        return db.query(Paciente).filter(Paciente.id == patient_id).first()

    @staticmethod
    def create(db: Session, payload: dict):
        patient = Paciente(**payload)
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def update(db: Session, patient: Paciente, payload: dict):
        for key, value in payload.items():
            setattr(patient, key, value)
        db.commit()
        db.refresh(patient)
        return patient

    @staticmethod
    def delete(db: Session, patient: Paciente):
        db.delete(patient)
        db.commit()

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.patient import PatientCreate, PatientResponse, PatientUpdate
from app.services.patient_service import PatientService

router = APIRouter(prefix="/pacientes", tags=["pacientes"])


@router.get("", response_model=list[PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    return PatientService.get_all(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient


@router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_patient(payload: PatientCreate, db: Session = Depends(get_db)):
    return PatientService.create(db, payload.model_dump())


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(
    patient_id: int,
    payload: PatientUpdate,
    db: Session = Depends(get_db),
):
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return PatientService.update(db, patient, payload.model_dump())


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = PatientService.get_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    PatientService.delete(db, patient)
    return None

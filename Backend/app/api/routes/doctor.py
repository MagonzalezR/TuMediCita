from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.doctor import DoctorCreate, DoctorResponse, DoctorUpdate
from app.services.doctor_service import DoctorService

router = APIRouter(prefix="/doctores", tags=["doctor"])


@router.get("", response_model=list[DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    return DoctorService.get_all(db)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = DoctorService.get_by_id(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor


@router.post(
    "",
    response_model=DoctorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_doctor(payload: DoctorCreate, db: Session = Depends(get_db)):
    return DoctorService.create(db, payload.model_dump())


@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor(
    doctor_id: int,
    payload: DoctorUpdate,
    db: Session = Depends(get_db),
):
    doctor = DoctorService.get_by_id(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return DoctorService.update(db, doctor, payload.model_dump())


@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = DoctorService.get_by_id(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    DoctorService.delete(db, doctor)
    return None

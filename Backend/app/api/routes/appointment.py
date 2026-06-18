from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentResponse
from app.services.appointment_service import AppointmentService

router = APIRouter(prefix="/citas", tags=["citas"])


@router.get("", response_model=list[AppointmentResponse])
def list_appointments(
    doctor_id: int | None = Query(default=None, alias="doctorId"),
    db: Session = Depends(get_db),
):
    return AppointmentService.get_all(db, doctor_id)


@router.post(
    "",
    response_model=AppointmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_appointment(
    payload: AppointmentCreate,
    db: Session = Depends(get_db),
):
    return AppointmentService.create(db, payload.model_dump())


@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = AppointmentService.get_by_id(db, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    AppointmentService.delete(db, appointment)
    return None
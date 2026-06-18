from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.doctor import DoctorResponse
from app.schemas.patient import PatientResponse


class AppointmentBase(BaseModel):
    paciente_id: int = Field(alias="pacienteId")
    doctor_id: int = Field(alias="doctorId")
    fecha: datetime
    motivo: str
    estado: str = "PROGRAMADA"

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        serialize_by_alias=True,
    )


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    paciente: PatientResponse | None = None
    doctor: DoctorResponse | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        serialize_by_alias=True,
    )

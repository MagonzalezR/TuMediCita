from pydantic import BaseModel, ConfigDict, Field

from app.schemas.specialty import SpecialtyResponse


class DoctorBase(BaseModel):
    nombres: str
    apellidos: str
    documento: str
    telefono: str
    email: str
    especialidad_id: int = Field(alias="especialidad_id")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        serialize_by_alias=True,
    )


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int
    especialidad: SpecialtyResponse | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        serialize_by_alias=True,
    )

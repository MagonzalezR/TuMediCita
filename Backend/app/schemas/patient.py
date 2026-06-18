from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class PatientBase(BaseModel):
    nombres: str
    apellidos: str
    documento: str
    fecha_nacimiento: date = Field(alias="fechaNacimiento")
    telefono: str
    email: str
    direccion: str

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        serialize_by_alias=True,
    )


class PatientCreate(PatientBase):
    pass


class PatientUpdate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        serialize_by_alias=True,
    )

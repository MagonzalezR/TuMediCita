from pydantic import BaseModel, ConfigDict


class SpecialtyBase(BaseModel):
    nombre: str


class SpecialtyCreate(SpecialtyBase):
    pass


class SpecialtyResponse(SpecialtyBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

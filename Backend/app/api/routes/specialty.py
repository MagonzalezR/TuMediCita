from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.specialty import SpecialtyCreate, SpecialtyResponse
from app.services.specialty_service import SpecialtyService

router = APIRouter(prefix="/especialidades", tags=["especialidades"])


@router.get("", response_model=list[SpecialtyResponse])
def list_specialties(db: Session = Depends(get_db)):
    return SpecialtyService.get_all(db)


@router.post(
    "",
    response_model=SpecialtyResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_specialty(payload: SpecialtyCreate, db: Session = Depends(get_db)):
    return SpecialtyService.create(db, payload.model_dump())

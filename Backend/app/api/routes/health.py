from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.health import HealthResponse
from app.services.health_service import HealthService

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse)
def read_health(db: Session = Depends(get_db)):
    db_ok = HealthService.check_db(db)
    return {
        "status": "ok" if db_ok else "degraded",
        "app": "TuMediCita API",
    }

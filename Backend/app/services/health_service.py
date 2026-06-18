from sqlalchemy.orm import Session

from app.models.health import HealthCheck


class HealthService:
    @staticmethod
    def check_db(session: Session) -> bool:
        try:
            session.query(HealthCheck).first()
            return True
        except Exception:
            return False

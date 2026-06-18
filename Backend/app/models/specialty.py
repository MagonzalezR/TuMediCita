from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Especialidad(Base):
    __tablename__ = "especialidad"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

    doctores = relationship("Doctor", back_populates="especialidad")

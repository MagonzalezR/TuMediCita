from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    documento = Column(String(20), unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(120), nullable=False)
    especialidad_id = Column(Integer, ForeignKey("especialidad.id"), nullable=False)

    especialidad = relationship("Especialidad", back_populates="doctores")
    citas = relationship("Cita", back_populates="doctor")

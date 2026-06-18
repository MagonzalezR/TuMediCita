from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Cita(Base):
    __tablename__ = "cita"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctor.id"), nullable=False)
    fecha = Column(DateTime, nullable=False, default=datetime.utcnow)
    motivo = Column(String(255), nullable=False)
    estado = Column(String(20), nullable=False, default="PROGRAMADA")

    paciente = relationship("Paciente", back_populates="citas")
    doctor = relationship("Doctor", back_populates="citas")

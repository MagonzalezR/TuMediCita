from datetime import date

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    documento = Column(String(20), unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(120), nullable=False)
    direccion = Column(String(255), nullable=False)

    citas = relationship("Cita", back_populates="paciente")

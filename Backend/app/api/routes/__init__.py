"""Rutas principales de la API."""
from fastapi import APIRouter

from app.api.routes.appointment import router as appointment_router
from app.api.routes.doctor import router as doctor_router
from app.api.routes.health import router as health_router
from app.api.routes.patient import router as patient_router
from app.api.routes.specialty import router as specialty_router

router = APIRouter()
router.include_router(health_router)
router.include_router(specialty_router)
router.include_router(patient_router)
router.include_router(doctor_router)
router.include_router(appointment_router)

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError

from app.api import routes
from app.core.config import settings
from app.core.database import Base, engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.on_event("startup")
def startup_event():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Base de datos inicializada correctamente.")
    except OperationalError as exc:
        logger.warning(
            "No se pudo conectar a la base de datos durante el startup: %s",
            exc,
        )


@app.get("/")
def root():
    return {
        "message": "Bienvenido a TuMediCita API",
        "docs": "/docs",
    }

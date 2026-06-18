# TuMediCita

## Prueba Tecnica de ingreso OATI - UD
Se quiere registrar usuarios pacientes para ser atendidos por doctores, previamente registrados, a través de una cita médica.
Debe guardarse información básica del paciente. Al
momento de solicitar/asignar la cita médica, debe permitir seleccionar un doctor y su
especialidad (no es obligatorio manejar horarios, consultorios, etc.). Se debe permitir listar los
doctores con sus citas y pacientes, modificar la información básica de un doctor o un
paciente, así como la opción de eliminar una cita médica.

El modelo consta de las entidades: paciente, doctor, cita.

Aplicación web completa para gestionar pacientes, doctores, especialidades y citas médicas, con un backend en FastAPI y un frontend en Angular.

## Objetivo del proyecto

Permitir registrar pacientes, administrar doctores y especialidades, y crear o eliminar citas médicas. El sistema debe soportar la visualización de doctores con sus citas y pacientes, además de la edición de información básica de pacientes y doctores.

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Frontend | Angular 19, TypeScript, RxJS, SCSS |
| Backend | Python, FastAPI, SQLAlchemy, Pydantic |
| Base de datos | PostgreSQL |
| Despliegue sugerido | Frontend: Vercel · Backend: Vercel · BD: Supabase |

## Estructura del proyecto

```text
Backend/
  app/
    api/
      routes/
    core/
    models/
    schemas/
    services/

Frontend/
  src/
    app/
      core/
      features/
      shared/
    environments/
```

## Modelo de negocio

- **Paciente**: datos personales, documento, fecha de nacimiento, teléfono, correo y dirección.
- **Doctor**: nombre, documento, contacto y especialidad asociada.
- **Especialidad**: catálogo para clasificar doctores.
- **Cita**: relación entre paciente y doctor, con fecha, motivo y estado.

## Diagrama de relaciones

```mermaid
erDiagram
    ESPECIALIDAD ||--o{ DOCTOR : tiene
    PACIENTE ||--o{ CITA : agenda
    DOCTOR ||--o{ CITA : atiende
```

# Backend

## Requisitos

- Python 3.12.5
- PostgreSQL (para funcionamiento real con la base de datos)
- Dependencias definidas en `Backend/requirements.txt`

## Instalación

```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Variables de entorno

Crear un archivo `.env` en la carpeta `Backend` (o ajustar la configuración según el entorno) con valores como:

```env
DATABASE_URL=postgresql+psycopg://usuario:password@host:5432/nombre_db
```

Si no se define `DATABASE_URL`, la configuración intentará usar los valores por defecto del archivo de configuración.

## Ejecutar la API

```bash
cd Backend
uvicorn app.main:app --reload
```

La API estará disponible en:

- http://localhost:8000/docs
- http://localhost:8000/api/v1/health

## Endpoints esperados

```http
GET    /api/v1/especialidades
POST   /api/v1/especialidades

GET    /api/v1/pacientes
GET    /api/v1/pacientes/{id}
POST   /api/v1/pacientes
PUT    /api/v1/pacientes/{id}
DELETE /api/v1/pacientes/{id}

GET    /api/v1/doctores
GET    /api/v1/doctores/{id}
POST   /api/v1/doctores
PUT    /api/v1/doctores/{id}
DELETE /api/v1/doctores/{id}

GET    /api/v1/citas?doctorId={id}
POST   /api/v1/citas
DELETE /api/v1/citas/{id}
```

# Frontend

## Requisitos

- Node.js 20+
- npm
- Un backend FastAPI corriendo en la URL configurada en el archivo de entorno del frontend

## Instalación

```bash
cd Frontend
npm install
```

## Variables de entorno

El frontend usa un archivo `.env` con las URLs y parámetros necesarios para la API:

```env
NG_APP_API_URL=http://localhost:8000
NG_APP_VERSION=1.0.0
```

## Ejecutar en desarrollo

```bash
cd Frontend
npm start
```

La aplicación quedará disponible en:

- http://localhost:4200

## Compilar para producción

```bash
cd Frontend
npm run build:prod
```

Los archivos generados se almacenan en `dist/citas-medicas-frontend`.

## Flujo recomendado para ejecutar el proyecto completo

1. Levantar la base de datos.
2. Iniciar el backend desde `Backend`.
3. Configurar el archivo `.env` del frontend.
4. Ejecutar el frontend desde `Frontend`.

## Despliegue sugerido

- **Frontend**: Vercel.
- **Backend**: Vercel.
- **Base de datos**: PostgreSQL administrado en Supabase.

# Ecommerce Backend (FastAPI)

## Tech Stack

- FastAPI
- Pydantic Settings for configuration
- SQLAlchemy 2.x (async) with SQLite by default
- Uvicorn for ASGI server

## Project Structure

```text
app/
  main.py            # FastAPI application factory and entrypoint
  core/              # Settings, security, shared core utilities
  api/               # API layer (dependencies, versioned routers)
    v1/
      router.py      # Root API router for v1
      health.py      # Health check endpoint
  db/                # Database engine / session
  models/            # SQLAlchemy models
  schemas/           # Pydantic models (request/response)
  services/          # Business logic
  repositories/      # Data access layer
  tests/             # Tests
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
```

## Running the server

```bash
uvicorn app.main:app --reload
```

The API docs will be available at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Environment variables

Configuration is managed via `.env` or environment variables. See `app/core/config.py` for available settings.

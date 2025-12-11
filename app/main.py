import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.router import api_router as api_v1_router
from app.core.config import settings
from app.db.session import Base, engine


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    media_root = os.path.join(os.getcwd(), "media")
    os.makedirs(media_root, exist_ok=True)
    application.mount("/media", StaticFiles(directory=media_root), name="media")

    application.include_router(api_v1_router, prefix=settings.API_V1_STR)

    @application.on_event("startup")
    async def on_startup() -> None:  # type: ignore[func-returns-value]
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    return application


app = create_application()

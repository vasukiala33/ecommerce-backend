from fastapi import FastAPI

from app.api.v1.router import api_router as api_v1_router
from app.core.config import settings
from app.db.session import Base, engine


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )

    # Include versioned API router
    application.include_router(api_v1_router, prefix=settings.API_V1_STR)

    @application.on_event("startup")
    async def on_startup() -> None:  # type: ignore[func-returns-value]
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    return application


app = create_application()

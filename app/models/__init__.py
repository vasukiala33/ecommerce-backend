from app.db.session import Base

# Import models here so Alembic / metadata can see them
from app.models.user import User  # noqa: F401

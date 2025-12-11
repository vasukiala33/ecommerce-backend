from app.db.session import Base

# Import models here so Alembic / metadata can see them
from app.models.user import User  # noqa: F401
from app.models.product import Product  # noqa: F401
from app.models.category import Category  # noqa: F401

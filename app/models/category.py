from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(length=255), unique=True, nullable=False)
    created_at = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import mapped_column

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(length=255), nullable=False)
    email = mapped_column(String(length=255), unique=True, index=True, nullable=False)
    hashed_password = mapped_column(String(length=255), nullable=False)
    role = mapped_column(String(length=50), default="customer", nullable=False)
    is_active = mapped_column(Boolean, default=True, nullable=False)
    created_at = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

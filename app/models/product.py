from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import mapped_column, relationship

from app.db.session import Base


class Product(Base):
    __tablename__ = "products"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String(length=255), nullable=False)
    description = mapped_column(Text, nullable=True)
    price = mapped_column(Numeric(10, 2), nullable=False)
    stock = mapped_column(Integer, default=0, nullable=False)
    seller_id = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    category_id = mapped_column(ForeignKey("categories.id"), nullable=False, index=True)
    created_at = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    seller = relationship("User", backref="products")
    category = relationship("Category", backref="products")

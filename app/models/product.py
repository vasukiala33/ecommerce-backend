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
    images = relationship(
        "ProductImage",
        back_populates="product",
        cascade="all, delete-orphan",
    )


class ProductImage(Base):
    __tablename__ = "product_images"

    id = mapped_column(Integer, primary_key=True, index=True)
    product_id = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    image_url = mapped_column(String(length=512), nullable=False)
    created_at = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    product = relationship("Product", back_populates="images")

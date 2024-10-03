from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text
# from app.db.base import Base_


from app.db.base_class import Base_


class Items(Base_):
    """Product whose price we are tracking"""
    __tablename__ = "Item"
    name: Mapped[str] = mapped_column(String(40), index=True, nullable=False)
    price: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    link:Mapped[str] = mapped_column(String(255), nullable=False)
    prices: Mapped[List["Price"]] = relationship(back_populates="price")

class Price(Base_):
    """History prices"""
    __tablename__ = "Price"
    product_id: Mapped[int] = mapped_column(ForeignKey("Item.id"))
    price: Mapped[str] = mapped_column(String(30), nullable=False)



from typing import Any
from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, declared_attr, DeclarativeBase, mapped_column

from app.utils.idgen import idgen


class Base_(DeclarativeBase):
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[str] = mapped_column(primary_key=True, default=idgen,index=True)
    created_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional
from sqlalchemy import func
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[Optional[str]]
    due_date: Mapped[datetime]
    done: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(default=func.now())

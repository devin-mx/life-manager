from sqlalchemy import select
from db.database import SessionLocal
from db.models import Task
from datetime import datetime


def add_task(title: str, due_date: datetime, description: str = ""):
    task = Task(title=title, description=description, due_date=due_date)
    session = SessionLocal()
    try:
        session.add(task)
        session.commit()
    finally:
        session.close()


def get_all_tasks():
    session = SessionLocal()
    try:
        tasks = session.execute(select(Task)).scalars().all()
        return tasks
    finally:
        session.close()

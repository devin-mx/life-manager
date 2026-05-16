from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = Path.home() / ".life-manager" / "data.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)

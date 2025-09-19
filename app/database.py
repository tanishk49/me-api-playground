from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database (file: app.db in project root)
DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency (we’ll use this in routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

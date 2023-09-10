from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Database setup
DATABASE_URL = "sqlite:///./test.db"  # This is just a placeholder; replace with your actual database URL
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=True)
Session = scoped_session(SessionLocal)

Base = declarative_base()

# Import models so they are registered with Base
from .user import User
from .profile import Profile
from .search_history import SearchHistory
from .email_notifications import EmailNotifications

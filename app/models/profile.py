from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    first_name = Column(String)
    last_name = Column(String)
    bio = Column(String)
    profile_picture = Column(String)
    date_of_birth = Column(DateTime)
    user = relationship("User", back_populates="profile")

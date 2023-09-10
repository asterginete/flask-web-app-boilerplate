from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    date_registered = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    profile = relationship("Profile", uselist=False, back_populates="user")
    search_histories = relationship("SearchHistory", back_populates="user")
    email_notifications = relationship("EmailNotifications", back_populates="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


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


class SearchHistory(Base):
    __tablename__ = 'search_histories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    query = Column(String, nullable=False)
    date_searched = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="search_histories")


class EmailNotifications(Base):
    __tablename__ = 'email_notifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    email_type = Column(String)
    date_sent = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="email_notifications")

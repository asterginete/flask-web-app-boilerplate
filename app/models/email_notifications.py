from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class EmailNotifications(Base):
    __tablename__ = 'email_notifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    email_type = Column(String)
    date_sent = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="email_notifications")

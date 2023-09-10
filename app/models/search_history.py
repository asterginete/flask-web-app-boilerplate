from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SearchHistory(Base):
    __tablename__ = 'search_histories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    query = Column(String, nullable=False)
    date_searched = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="search_histories")

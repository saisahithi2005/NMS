from sqlalchemy import Column, Integer, String
from database import Base


class LogEntry(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)


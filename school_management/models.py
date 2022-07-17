from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from .database import Base


# class BaseModel(Model): pass


# created_at = Column(DateTime(timezone=True),
#                     server_default=datetime.datetime.now())


class Student(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)

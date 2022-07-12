from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from .database import Model


class BaseModel(Model):
    created_at = Column(DateTime(timezone=True),
                        server_default=datetime.datetime.now())


class Student(BaseModel):
    __tablename__ = "user"

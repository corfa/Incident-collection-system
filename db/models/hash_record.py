from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db.models.base import BaseModel


class HashRecord(BaseModel):
    __tablename__ = "hash_records"

    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    problem = relationship("Problem", back_populates="hash_records")
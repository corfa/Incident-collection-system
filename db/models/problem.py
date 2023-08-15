from sqlalchemy import Column, Integer, JSON
from sqlalchemy.orm import relationship

from db.models.base import BaseModel


class Problem(BaseModel):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    headers = Column(JSON)
    body = Column(JSON)
    hash_records = relationship("HashRecord", back_populates="problem")

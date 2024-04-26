from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Bandwidth(Base):
    __tablename__ = "bandwidth"

    id = Column(Integer, primary_key=True)
    upload = Column(Float)
    download = Column(Float)
    time = Column(String)


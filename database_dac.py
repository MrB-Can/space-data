from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SpaceObjects(Base):
    __tablename__ = "iss_tle"

    id = Column(Integer, primary_key=True)



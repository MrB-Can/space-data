from sqlalchemy import Column, Integer, DateTime, String, Float, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SpaceObjects(Base):
    __tablename__ = "iss_tle"

    id = Column(Integer, primary_key=True, nullable=False)
    record_time = Column(DateTime, nullable=False)


class NORADInfo(Base):
    __tablename__ = "norad_list"

    id = Column(Integer, primary_key=True, nullable=False)
    record_time = Column(DateTime)
    object_name = Column(String)
    object_id = Column(String)
    object_type = Column(String)
    ops_status_code = Column(String)
    owner = Column(String)
    launch_date = Column(DateTime)
    launch_site = Column(String)
    decay_date = Column(DateTime)
    period = Column(Float)
    inclination = Column(Float)
    apogee = Column(Integer)
    perigee = Column(Integer)
    rcs = Column(Float)
    data_status_code = Column(String)
    orbit_center = Column(String)
    orbit_type = Column(String)



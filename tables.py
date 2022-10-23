from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    checks = relationship("Check")


class Check(Base):
    __tablename__ = "check"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    parent_id = Column(Integer, ForeignKey("user_table.id"))

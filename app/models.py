from sqlalchemy import Column, Integer, String


from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    name = Column(String(50), index=True)
    position = Column(String(50))
    skills = Column(String(50))

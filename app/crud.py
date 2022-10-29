from operator import and_
from turtle import position
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_login(db: Session, email: str, password: str):
    userm = db.query(models.User).filter(and_(models.User.email == email, models.User.password == password)).first()
    return userm



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(name=user.name, email=user.email, password=user.password, position=user.position, skills=user.skills)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



# Docs:
# https://dataarch.medium.com/fastapi-and-sqlalchemy-conundrum-and-or-or-49e9fa6787b0
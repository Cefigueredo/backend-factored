from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
import json 
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





# Dependency
def get_db():
    db = SessionLocal()

    # // '{"Python": "70", "SQL": "80", "Api Rest": "80", "Java": "73", "React": "56"}' // This works in python
    # "{'Python': 70, 'SQL': 80, 'Api Rest': 80, 'Java': 73, 'React': 56}"
    # "{\"Python\": 70, \"SQL\": 80, \"Api Rest\": 80, \"Java\": 73, \"React\": 56}" // This works in postman
    # Dummy data
    FIRST_USER = "ce.figueredo@gmail.com" 
    if FIRST_USER:
        user = crud.get_user_by_email(db, email=FIRST_USER) 
        if not user:
            dictionary = {"Python": 70, "SQL": 80, "Api Rest": 80, "Java": 73, "React": 56}
            json_object = json.dumps(dictionary, indent = 4) 
            user_in = schemas.User(    
                email=FIRST_USER,
                password="password",
                position="Engineer",
                skills=json_object,
                name="Carlos Figueredo"
            )
            try:
                crud.create_user(db, user_in)
            except:
                raise HTTPException(status_code=201, detail="Done")
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/", response_model=schemas.User)
def log_user(email: str, password: str, db: Session = Depends(get_db)):
    if email=="" or email is None or password=="" or password is None:
        raise HTTPException(status_code=512, detail="Bad request")

    db_user = crud.get_user_login(db, email=email, password=password)

    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found")
    



#Docs:
# https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_4_2
# https://fastapi.tiangolo.com/tutorial/cors/
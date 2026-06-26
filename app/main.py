from fastapi import FastAPI
from app.routers.employee import router
from app.database import create_tables
from fastapi import FastAPI
from app.database import Base, engine
from app import models

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def home():
    return {"message": "Welcome"}

app.include_router(router)
Base.metadata.create_all(bind=engine)
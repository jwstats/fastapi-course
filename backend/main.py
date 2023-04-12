from fastapi import FastAPI
from core.config import settings
from db.sessions import engine
from db.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, varion=settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()

@app.get("/")
def hello_api():
    return {"message":"Hello World"}
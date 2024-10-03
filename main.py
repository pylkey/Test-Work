from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine 
# from app.db.base_class import Base_
from app.db.base import Base_


def create_tables():         
	Base_.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}
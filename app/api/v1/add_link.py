from fastapi import APIRouter, BackgroundTasks
from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas.product import ProductCreate
from app.db.session import get_db


router = APIRouter()


@router.post("/")
async def scrapy_product_data(background_tasks: BackgroundTasks, db:Session = Depends(get_db)):
    background_tasks.add_task(
        
    )
    return {"message": "Product add to DB in the background"}
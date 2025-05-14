
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.sales_schema import SaleCreate, SaleRead
from app.controllers.data_controller import DataController
from typing import List
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/seed", status_code=201)
def seed_data(current_user: str = Depends(get_current_user)):
    DataController.seed_sales_data()
    return {"message": "Data seeded successfully"}

@router.get("/sales", response_model=List[SaleRead])
def get_all_sales(current_user: str = Depends(get_current_user)):
    return DataController.get_sales()

@router.post("/sales", response_model=SaleRead)
def create_sale(sale: SaleCreate, current_user: str = Depends(get_current_user)):
    return DataController.create_sale(sale)

@router.get("/search")
def search_sales(q: str, current_user: str = Depends(get_current_user)):
    return DataController.search_sales(q)
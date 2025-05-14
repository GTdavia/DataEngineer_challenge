from app.db.database import get_session
from app.db.models.fact_sales import FactVenta
from sqlmodel import select
from typing import List
from app.schemas.sales_schema import SaleCreate

class SalesRepository:

    @staticmethod
    def get_all() -> List[FactVenta]:
        with next(get_session()) as session:
            return session.exec(select(FactVenta)).all()

    @staticmethod
    def insert_one(sale: SaleCreate) -> FactVenta:
        with next(get_session()) as session:
            venta = FactVenta(**sale.dict())
            session.add(venta)
            session.commit()
            session.refresh(venta)
            return venta
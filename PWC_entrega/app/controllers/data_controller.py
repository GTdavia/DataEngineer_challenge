from app.db.repository import SalesRepository
from app.schemas.sales_schema import SaleCreate
from app.services.etl import load_csv_to_db
from app.services.search_service import search_in_vector_db

class DataController:

    @staticmethod
    def seed_sales_data():
        load_csv_to_db("data/sales_data.csv")

    @staticmethod
    def get_sales():
        return SalesRepository.get_all()

    @staticmethod
    def create_sale(sale: SaleCreate):
        return SalesRepository.insert_one(sale)

    @staticmethod
    def search_sales(query: str):
        return search_in_vector_db(query)
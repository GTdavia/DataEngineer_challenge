import pandas as pd
from app.db.models.fact_sales import FactVenta
from app.db.database import get_session


def load_csv_to_db(filepath: str):
    df = pd.read_csv(filepath)
    with next(get_session()) as session:
        for _, row in df.iterrows():
            venta = FactVenta(**row.to_dict())
            session.add(venta)
        session.commit()
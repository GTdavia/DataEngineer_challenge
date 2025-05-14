from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False)

def init_db():
    from app.db.models import fact_sales, dimensions  # importa modelos para registrar
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
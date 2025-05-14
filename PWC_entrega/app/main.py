from fastapi import FastAPI
from app.api.v1.endpoints import router as v1_router
from app.db.database import init_db

app = FastAPI(title="Data Engineering Challenge")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(v1_router, prefix="/api/v1")
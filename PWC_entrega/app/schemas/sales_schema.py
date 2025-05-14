from pydantic import BaseModel
from typing import Optional

class SaleCreate(BaseModel):
    producto_id: str
    cliente_id: str
    fecha: str
    categoria: str
    producto: str
    precio_unitario: float
    cantidad: int
    total: float

class SaleRead(SaleCreate):
    id: Optional[int]
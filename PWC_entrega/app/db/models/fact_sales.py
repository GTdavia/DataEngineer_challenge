python
from sqlmodel import SQLModel, Field
from typing import Optional

class FactVenta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    producto_id: str
    cliente_id: str
    fecha: str
    categoria: str
    producto: str
    precio_unitario: float
    cantidad: int
    total: float
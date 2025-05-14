from sqlmodel import SQLModel, Field
from typing import Optional

class DimProducto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    producto_id: str
    nombre: str
    categoria: str

class DimCliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: str

class DimTiempo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: str
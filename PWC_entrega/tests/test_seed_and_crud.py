import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_seed_data():
    response = client.post("/api/v1/seed", auth=("admin", "admin123"))
    assert response.status_code == 201
    assert response.json()["message"] == "Data seeded successfully"

def test_create_and_get_sale():
    sale = {
        "producto_id": "abc123",
        "cliente_id": "cli456",
        "fecha": "2024-01-01",
        "categoria": "Electrónica",
        "producto": "Laptop",
        "precio_unitario": 999.99,
        "cantidad": 1,
        "total": 999.99
    }
    create = client.post("/api/v1/sales", json=sale, auth=("admin", "admin123"))
    assert create.status_code == 200
    created = create.json()
    assert created["producto"] == "Laptop"

    get_all = client.get("/api/v1/sales", auth=("admin", "admin123"))
    assert get_all.status_code == 200
    assert any(s["producto"] == "Laptop" for s in get_all.json())
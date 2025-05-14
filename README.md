# CANDIDATO
## Gonzalo Javier Teruggi

# 🚀 Data Engineering Challenge

Este proyecto implementa una solución integral de ingeniería de datos con arquitectura tipo Data Lakehouse. Incluye un sistema ETL, almacenamiento estructurado en múltiples capas (Bronze, Silver, Gold), búsqueda textual rápida usando Typesense y exposición de servicios a través de una API REST construida con FastAPI.

---

## 🧱 Arquitectura

El sistema sigue la **Medallion Architecture** con un enfoque en esquemas en estrella (Star Schema):

- **Bronze Layer**: datos crudos desde un archivo CSV (`sales_data.csv`)
- **Silver Layer**: tablas de dimensiones normalizadas (`dim_producto`, `dim_cliente`, `dim_tiempo`)
- **Gold Layer**: tabla de hechos (`fact_ventas`) para análisis y reporting

> También incluye integración con una Vector DB (Typesense) para búsquedas rápidas por texto.

---

## 🛠️ Tecnologías utilizadas

- FastAPI
- SQLModel + SQLite
- Pandas (ETL)
- Typesense (Vector DB)
- Docker + Docker Compose
- Pytest (Testing)
- Pydantic (Validación)
- Mermaid.js (Diagramas)
- Autenticación HTTP Basic

---

## 📂 Estructura del Proyecto

```
data_engineering_challenge/
├── app/
│   ├── api/v1/
│   ├── controllers/
│   ├── core/
│   ├── db/models/
│   ├── db/
│   ├── schemas/
│   └── services/
├── data/
├── diagrams/
├── tests/
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## 🚀 Cómo levantar el proyecto

### 🔧 Requisitos

- Docker y Docker Compose
- (Opcional) Python 3.10+ y Poetry

### ▶️ Instrucciones rápidas

```bash
docker-compose up --build
```

### Acceso a la documentación interactiva

Una vez desplegado, acceder a:
```
http://localhost:8000/docs
```

> Login: `admin` / `admin123`

---

## 🔍 Endpoints disponibles

- `POST /api/v1/seed`: carga el CSV en la base de datos
- `POST /api/v1/sales`: crea una venta nueva
- `GET /api/v1/sales`: lista todas las ventas
- `GET /api/v1/search?q=...`: búsqueda textual con Typesense

---

## ✅ Testing

Para ejecutar los tests:

```bash
pytest tests/
```

---

## 📊 Diagramas

Los diagramas Mermaid están en `diagrams/`:

- `architecture.mmd`: flujo general
- `bronze_layer.mmd`, `silver_layer.mmd`, `gold_layer.mmd`: capas del lago

Visualizalos en [Mermaid Live Editor](https://mermaid.live/edit).

---

## 📄 Licencia

MIT © Tu Nombre

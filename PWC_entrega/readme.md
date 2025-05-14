# Data Engineering Challenge

Este proyecto implementa una arquitectura de Data Lakehouse con FastAPI, Typesense, y SQLModel.

## Estructura

- **Bronze Layer**: `CSV` crudo
- **Silver Layer**: dimensiones normalizadas
- **Gold Layer**: tabla de hechos agregada

## Features

- ETL desde CSV
- CRUD completo
- Búsqueda textual (Typesense)
- Arquitectura Medallion + Star Schema
- Autenticación con Basic Auth
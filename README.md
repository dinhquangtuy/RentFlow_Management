# 🏢 RentFlow - Rental Property Management API

> A modern backend system for rental properties with automated VietQR billing and webhook payment reconciliation.

## 📌 Overview
Managing rental apartments and mini-condos usually requires manual utility recording and tedious banking checks. 

**RentFlow** automates the entire process:
- Calculates electricity and water bills automatically.
- Generates dynamic VietQR codes for instant payment.
- Reconciles bank transfers in real-time via Webhooks.

## 🛠️ Tech Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (High-performance async Python backend)
- **Server**: [Uvicorn](https://www.uvicorn.org/) (Lightning-fast ASGI server)
- **Database & ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) with PostgreSQL / SQLite
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Payment Standard**: VietQR (Napas247) & Webhooks

## ⚡ Getting Started

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Setup Virtual Environment
```powershell
# Create virtual environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\Activate.ps1

# Install dependencies
pip install fastapi uvicorn
```

### 3. Run Development Server
```powershell
uvicorn app.main:app --reload
```
The server will be running at `http://127.0.0.1:8000`.

## 📖 API Documentation
Once the server is running, visit:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

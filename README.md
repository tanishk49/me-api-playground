# ME-API-PLAYGROUND

A FastAPI-based backend API playground for managing **Profiles**, **Projects**, and **Skills**.  
This project demonstrates CRUD operations, schema design, and API documentation using FastAPI + SQLAlchemy ORM.

---

## 🚀 Features
- FastAPI with automatic interactive docs (Swagger UI & ReDoc)
- SQLAlchemy ORM for database modeling
- SQLite (default) database (can be swapped with PostgreSQL/MySQL)
- CRUD operations for:
  - Profiles
  - Projects
  - Skills
- Seed script for sample data
- Human-readable schema (`schema.md`) and SQL schema (`schema.sql`)

---

## 📂 Project Structure
```text
ME-API-PLAYGROUND/
│── app/
│   │── crud.py          # CRUD logic
│   │── database.py      # Database engine & session
│   │── main.py          # FastAPI entry point
│   │── models.py        # SQLAlchemy models
│   │── schemas.py       # Pydantic schemas
│   │── seed.py          # Seed script for sample data
│   │── __init__.py
│── schema.md            # Human-readable schema (Markdown)
│── schema.sql           # SQL schema (DDL statements)
│── app.db               # SQLite database (local)
│── requirements.txt     # Python dependencies
│── LICENSE
│── README.md            
│── .gitignore
│── .venv/               # Virtual environment
```

---

## 📜 Database Schema
The database schema is defined using SQLAlchemy ORM.  
- [schema.md](schema.md) — human-readable documentation  
- [schema.sql](schema.sql) — SQL DDL statements  


## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanishk49/ME-API-PLAYGROUND.git
   cd ME-API-PLAYGROUND

2. **Create & activate virtual environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Linux/Mac
    .venv\Scripts\activate      # On Windows  
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**
   ```bash
   uvicorn app.main:app --reload



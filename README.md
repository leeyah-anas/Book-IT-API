# Book-IT-API
A FastAPI booking system built for managing service appointments with user authentication and admin controls.

## Features

- User registration & authentication (JWT)
- Service listing and booking
- Booking status management
- User reviews for services
- PostgreSQL database with SQLAlchemy ORM
- Alembic for database migrations
- Dockerized for easy development

## Requirements

- Python 3.10+
- PostgreSQL
- Docker (optional, for containerized setup)
  
## Why PostgreSQL (Relational / SQL)

1.Structured Data & Relationships

- Perfect if your data is tabular (users, orders, products, events, etc.) and entities are related (e.g., a user has many orders).

- Enforces schema & constraints → reduces bad data.

2.Complex Queries

- SQL is powerful for joins, aggregations, analytics.

3.Transactions (ACID)

- it ensures consistency; Banking, booking systems, inventory — where consistency matters.

4.Ecosystem & Extensions

JSON support, PostGIS (geo queries), full-text search, time-series.

Strong tooling (DBeaver, pgAdmin, ORM support like SQLAlchemy).

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/Book-IT-API.git
cd bookit-api
```

### 2. Configure Environment Variables

Edit the `.env` file with your database credentials:

```
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/bookitdb
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
ENVIRONMENT=development
LOG_LEVEL=INFO
```
### 3. Activate venv

```sh
py -m venv venv

venv\Scripts\activate
```

### 4. Install Dependencies

```sh
pip install -r requirements.txt
```

### 5. Run Database Migrations

```sh
alembic upgrade head
```
### 6. Create Admin
```sh
python -m app.create_admin
```

### 7. Start the API

```sh
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

---

## Project Structure

```
app/
  ├── main.py
  ├── models/
  ├── routers/
  ├── schemas/
  ├── database.py
  ├── config.py
alembic/
  ├── versions/
  ├── env.py
requirements.txt
.env

```

---

## License

MIT

---

## Author

Anataku Aaliyah

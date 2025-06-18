# Task Management API

A modern task and project management backend built using **FastAPI**, **PostgreSQL**, and **Docker**. Supports role-based access control with three user roles: `admin`, `manager`, and `user`.

---

## Features

- JWT-based authentication
- Role-based permissions (Admin, Manager, User)
- Project & Task CRUD
- Task assignments
- Commenting on tasks
- Secure user registration/login
- Asynchronous DB access with SQLAlchemy

---

## Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL 15
- SQLAlchemy (async)
- Alembic (migrations)
- Docker + Docker Compose

---

## Project Structure

```bash
TASK_MANAGEMENT_API/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── projects.py
│   │   │   ├── tasks.py
│   │   │   └── comments.py
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── auth.py
│   │
│   ├── db/
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── project.py
│   │   │   ├── task.py
│   │   │   └── comment.py
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── comment.py
│   │
│   ├── crud/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   └── comment.py
│   │
│   ├── main.py
│   └── init_db.py
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:prasanth-33460/Task-Management-API.git
cd task-management-api
```

### 2. Run with Docker

Make sure Docker and Docker Compose are installed.

```bash
docker-compose up --build
```

This will:

Spin up PostgreSQL (localhost:5432)

Run FastAPI app on <http://localhost:8000>

Apply Alembic migrations automatically

### 3. Run Locally (without Docker)

```bash
# Activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables (or use .env file)
export DATABASE_URL_LOCAL=postgresql+asyncpg://postgres:your_password@localhost:5432/taskdb
export SECRET_KEY=your-secret
export ALGORITHM=HS256
export ACCESS_TOKEN_EXPIRE_MINUTES=30

# Run migrations
alembic upgrade head

# Start the app
uvicorn app.main:app --reload
```

### Authentication

Use the /auth/register and /auth/login endpoints to obtain JWT tokens.

```bash
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=admin@example.com&password=secret
```

The response will include:

```bash
{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}
```

Use it in headers:

```bash
Authorization: Bearer JWT_TOKEN_HERE
```

API Endpoints
  Swagger UI: <http://localhost:8000/docs>
  ReDoc: <http://localhost:8000/redoc>

Auth
POST /auth/register

POST /auth/login

Users
GET /users/me

PUT /users/me

Projects
GET /projects/

POST /projects/

GET /projects/{id}

PUT /projects/{id}

DELETE /projects/{id}

Tasks
GET /projects/{project_id}/tasks/

POST /projects/{project_id}/tasks/

GET /projects/{project_id}/tasks/{task_id}

PUT /projects/{project_id}/tasks/{task_id}

DELETE /projects/{project_id}/tasks/{task_id}

PUT /projects/{project_id}/tasks/{task_id}/assign?user_id={id}

Comments
GET /tasks/{task_id}/comments/

POST /tasks/{task_id}/comments/

```bash
| Role    | Can Create Project  | Assign Tasks   | View All Tasks     | Comment |
| ------- | ------------------  | ------------   | --------------     | ------- |
| Admin   | ✅                  | ✅            | ✅                 | ✅     |
| Manager | ✅ (own)            | ✅            | ✅                 | ✅     |
| User    | ❌                  | ❌            | Assigned only      | ✅      |
```

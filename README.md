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

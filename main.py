from fastapi import FastAPI
from app.api.routes import health
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

import os
print("DEBUG: DATABASE_URL =", os.getenv("DATABASE_URL"))

from app.api.routes import (
    auth,
    users,
    projects,
    tasks,
    comments,
)

app = FastAPI(
    title="Task Management API",
    version="1.0.0",
    description="API for managing users, projects, tasks, and comments.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(comments.router)
app.include_router(health.router)

@app.get("/", tags=["Health"])
async def root():
    return {"message": "Task Management API is running"}

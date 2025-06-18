from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# Load environment variables only in local development
if os.getenv("GITHUB_ACTIONS") != "true":
    load_dotenv()

# Import Base for metadata
from app.db.base_class import Base
target_metadata = Base.metadata

from app.db import base  # type: ignore[reportUnusedImport]

# Alembic config
config = context.config

def get_database_url():
    """Get the appropriate database URL based on environment."""
    # In GitHub Actions
    if os.getenv("GITHUB_ACTIONS") == "true":
        # Use sync URL from environment or fallback
        return os.getenv("SYNC_DATABASE_URL") or \
               "postgresql://postgres:040783@localhost:5432/taskdb"
    
    # Local development
    db_url = os.getenv("DATABASE_URL_LOCAL") or os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError(
            "No database URL configured. "
            "Set either DATABASE_URL_LOCAL or DATABASE_URL environment variable."
        )
    return db_url.replace("postgresql+asyncpg", "postgresql")

# Set the database URL for Alembic
db_url = get_database_url()
config.set_main_option("sqlalchemy.url", db_url)

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
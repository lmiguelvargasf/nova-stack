# Freya Backend

Backend for Freya (part of a monorepo).

## Prerequisites

- [uv][]: Environment and package management
- [PostgreSQL][]: Database system

## Setup

Navigate to this service's directory within the monorepo.

**Install Dependencies:**

Create virtual environment and install dependencies:

```bash
uv sync
```

**Configure Environment:**

Copy the example environment file:

```bash
cp .env-example .env
```

**Database Setup:**

Create the database:

```bash
PGPASSWORD=postgres psql -U postgres -h localhost -c "CREATE DATABASE freya;"
```

Run migrations:

```bash
uv run --env-file .env piccolo migrations forward all
```

## Running the Application

To run the development server:

```bash
uv run --env-file .env litestar run
```

The server will be available at `http://127.0.0.1:8000`.

[uv]: https://docs.astral.sh/uv/
[PostgreSQL]: https://www.postgresql.org/

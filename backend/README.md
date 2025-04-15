# app

Backend for Freya (part of a monorepo).

## Prerequisites

- Python >=3.13
- [uv][] (for environment and package management)

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

## Running the Application

To run the development server:

```bash
uv run --env-file .env litestar run
```

The server will be available at `http://127.0.0.1:8000`.

[uv]: https://docs.astral.sh/uv/

# Freya Backend

This service is containerized via Docker Compose. See the [project root README](../README.md) for setup and running instructions.

## Access Backend

- Backend Admin UI: http://localhost:8000/admin/
- Backend Health Check: http://localhost:8000/health

## Linting & Formatting

This project uses [ruff][] for code linting and formatting.

#### Check and Auto-fix
Run `ruff` and automatically fix violations when possible.

```bash
uv run ruff check --force-exclude --fix
```

#### Format
Run `ruff`'s formatter.

```bash
uv run ruff format --force-exclude
```

[ruff]: https://docs.astral.sh/ruff/

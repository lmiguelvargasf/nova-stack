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

## Testing

This project uses [pytest][] for testing.

Run tests using pytest with the test database configuration:

```bash
PICCOLO_CONF=backend.config.piccolo_test pytest
```

[pytest]: https://docs.pytest.org/
[ruff]: https://docs.astral.sh/ruff/

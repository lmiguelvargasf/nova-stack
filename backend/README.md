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

This project uses [pytest][] for testing. Coverage is measured using [pytest-cov][] and an HTML report is generated in the [`htmlcov/`](./htmlcov) directory after running the tests.

### Running Tests without Coverage

Run tests using `pytest` without generating a coverage report.

```bash
PICCOLO_CONF=backend.config.piccolo_test uv run pytest --no-cov
```

### Running Tests with Coverage

Run tests with coverage, the following command generates a `.coverage` data file:

```bash
PICCOLO_CONF=backend.config.piccolo_test uv run pytest
```

### Running Tests with Coverage with HTML report

To generate an HTML report directly in the [`htmlcov/`](./htmlcov) directory while running tests, add the `--cov-report html` flag:

```bash
PICCOLO_CONF=backend.config.piccolo_test uv run pytest --cov-report html
```

[pytest]: https://docs.pytest.org/
[pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/
[ruff]: https://docs.astral.sh/ruff/

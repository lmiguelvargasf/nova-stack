# CI Workflow

This workflow runs automatically on:
- Push to the `main` branch
- Pull requests to the `main` branch

## Jobs

### Generate GraphQL Schema
- Builds the GraphQL schema from the backend
- Uploads it as an artifact for frontend use

### Frontend Lint and Test
- Runs in a Playwright container
- Uses `pnpm` for dependency management with caching
- Installs dependencies
- Downloads the GraphQL schema artifact
- Generates GraphQL code
- Runs linting, format checking, and tests

### Backend Lint and Test
- Uses a PostgreSQL service container
- Installs Python dependencies
- Runs `ruff` for linting and formatting
- Runs `pyright` for type checking
- Runs `pytest` for tests (without coverage)

# PR Validation Workflow

This workflow runs on pull request events (opened, synchronized, reopened, edited).

## Jobs

### Validate PR
- Checks PR title follows semantic conventions (`feat`, `fix`, `docs`, etc.)
- Validates PR size is 400 lines of code or less
- Comments on PRs that exceed the size threshold

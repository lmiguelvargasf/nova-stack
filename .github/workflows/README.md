# CI/CD Workflows

This directory contains GitHub Actions workflows for continuous integration and continuous deployment of the Nova Stack monorepo.

## Workflows

### CI Workflow (`ci.yml`)
Runs on push to main and pull requests to main branch. Performs:
- **Frontend**:
  - Linting with Biome
  - Format checking with Biome
  - Unit tests with Vitest
- **Backend**:
  - Linting with Ruff
  - Format checking with Ruff
  - Type checking with Pyright
  - Unit tests with Pytest

### CD Workflow (`cd.yml`)
Runs on push to main and when tags are created. Performs:
- Builds Docker images for both frontend and backend
- Pushes images to Docker Hub with appropriate tags
- Contains a commented deployment section that can be customized

### PR Validation (`pr-validation.yml`)
Runs on pull request events. Performs:
- Validates PR titles follow semantic convention
- Checks for large PRs and comments with a warning if needed

## Required Secrets

For these workflows to function properly, you need to set up the following secrets in your GitHub repository:

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token

## Deployment Configuration

To enable the deployment section in the CD workflow:
1. Uncomment the deployment job
2. Set up the following additional secrets:
   - `DEPLOY_HOST`: The hostname of your deployment server
   - `DEPLOY_USERNAME`: SSH username for your deployment server
   - `DEPLOY_SSH_KEY`: SSH private key for authentication

## Local Development

For local development and testing, you can use the Taskfile commands:
- `task backend:lint:fix` - Run linting on backend
- `task backend:test` - Run backend tests
- `task frontend:lint` - Run linting on frontend
- `task frontend:test:run` - Run frontend tests

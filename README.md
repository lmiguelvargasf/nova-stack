# Freya

A modern financial application to track spending, organize transactions, and visualize financial trends.

## Tech Stack

### Backend
- **[Python][python]** - Core programming language for backend.
- **[Litestar][litestar]** - High-performance ASGI framework for modern Python web apps.
- **[Piccolo][piccolo]** - Async ORM and query builder with migration support.
- **[PostgreSQL][postgresql]** - Advanced open-source relational database known for reliability.

### Frontend
- **[TypeScript][typescript]** - Core language for frontend, adding static types to JavaScript.
- **[Next.js][nextjs]** - React framework for production-ready applications
- **[Tailwind CSS][tailwind]** - Utility-first CSS framework for rapid UI development
- **[Chart.js][chartjs]** - Simple yet flexible JavaScript charting library

## Getting Started

### Prerequisites

The primary prerequisites for this project are:
- **[Docker Desktop][docker-desktop]:** Provides Docker Engine and Docker Compose.
- **[Task][task]:** A task runner / build tool used for managing common development workflows.

#### Alternative Installation

If you prefer not to use Docker Desktop, you can install the components separately:
- [**Docker Engine:**](https://docs.docker.com/engine/install/) Version 28 or later.
- [**Docker Compose:**](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually) Version 2 (V2) or later.

#### Verifying Installation

You can verify your installation by running:
```bash
docker --version
docker compose version
task --version
```

### Environment Setup

1. Copy the example environment files:
   ```bash
   cp .env.example .env
   cp backend/.env.example backend/.env
   cp frontend/.env.local.example frontend/.env.local
   ```

2. Edit the environment files (`.env`, `backend/.env`, and `frontend/.env.local`) to set your necessary secrets and configuration.

### Starting the Application

1. Build the Docker images:
   ```bash
   task build
   ```

2. Start all services:
   ```bash
   task up
   ```

3. The services will be available at:
   - Frontend Application: http://localhost:3000
   - Backend Admin UI: http://localhost:8000/admin/
   - Backend Health Check: http://localhost:8000/health

4. To stop and remove containers:
   ```bash
   task down
   ```

## Development Tasks

This project uses [Task][] as a task runner to simplify common development workflows. The main `Taskfile.yml` in the project root provides commands for:

- Managing the Docker environment (e.g., building images, starting/stopping services).
- Running development tasks within the `backend` and `frontend` services (e.g., linting, formatting, testing).

To see all available tasks and their descriptions, run the following command from the project root:

```bash
task --list
```

Refer to the `README.md` files in the [`backend`](./backend/README.md) and [`frontend`](./frontend/README.md) for service-specific task details.

## Deployment
...

## License
MIT

[chartjs]: https://www.chartjs.org/
[docker-desktop]: https://www.docker.com/products/docker-desktop/
[litestar]: https://litestar.dev/
[nextjs]: https://nextjs.org/
[piccolo]: https://piccolo-orm.com/
[postgresql]: https://www.postgresql.org/
[python]: https://www.python.org/
[tailwind]: https://tailwindcss.com/
[task]: https://taskfile.dev/
[typescript]: https://www.typescriptlang.org/

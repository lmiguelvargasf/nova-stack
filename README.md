# Nova Stack 🌟

![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge&logo=python)
![Node.js](https://img.shields.io/badge/node.js-22.14-brightgreen?style=for-the-badge&logo=node.js)
![Next.js](https://img.shields.io/badge/Next.js-15.x-black?style=for-the-badge&logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=for-the-badge&logo=typescript)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-0074D9?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0074D9?style=for-the-badge&logo=docker&logoColor=white)
![Task](https://img.shields.io/badge/Task-43B883?style=for-the-badge&logo=task&logoColor=white)

A modern full-stack application template built for quick and efficient project setup.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Development Tasks](#development-tasks)
- [License](#license)

## Tech Stack

### Backend
- **[Python][python]** – Core programming language for backend.
- **[Litestar][litestar]** – High-performance ASGI framework for modern Python web apps.
- **[Piccolo][piccolo]** – Async ORM and query builder with migration support.
- **[PostgreSQL][postgresql]** – Advanced open-source relational database known for reliability.

### Frontend
- **[TypeScript][typescript]** – Core language for frontend, adding static types to JavaScript.
- **[Next.js][nextjs]** – React framework for production-ready applications.
- **[Tailwind CSS][tailwind]** – Utility-first CSS framework for rapid UI development.
- **[Chart.js][chartjs]** – Simple yet flexible JavaScript charting library.

## Getting Started

### Prerequisites

The primary prerequisites for this project are:
- **[Docker Desktop][docker-desktop]:** Provides Docker Engine and Docker Compose.
- **[Task][task]:** A task runner / build tool used for managing common development workflows.

#### Alternative Installation

Alternatively, install the components separately:
- [**Docker Engine:**](https://docs.docker.com/engine/install/) Version 28 or later.
- [**Docker Compose:**](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually) Version 2 (V2) or later.

#### Verifying Installation

Verify the installation by running:
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

2. Edit the environment files (`.env`, `backend/.env`, and `frontend/.env.local`) to set the required secrets and configuration values (such as database URLs, API keys, etc.).

### Starting the Application

1. Build the Docker images:
   ```bash
   task docker:build
   ```

2. Start all services:
   ```bash
   task docker:up
   ```

3. The services will be available at:
   - Frontend application: http://localhost:3000
   - Backend admin UI: http://localhost:8000/admin/
   - Backend health check: http://localhost:8000/health

4. To stop and remove containers:
   ```bash
   task docker:down
   ```

## Development Tasks

This project uses [Task][] to simplify common development workflows. The main `Taskfile.yml` in the project root provides commands for:

- Managing the Docker environment (for example, building images, starting or stopping services).
- Running development tasks within the `backend` and `frontend` services (such as linting, formatting, or testing).

To list all available tasks, run:

```bash
task --list
```

Refer to the `README.md` files in the [`backend`](./backend/README.md) and [`frontend`](./frontend/README.md) directories for service-specific task details.

## License

This project is licensed under the [MIT License](./LICENSE).

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

# Freya

A modern financial application to track spending, organize transactions, and visualize financial trends.

## Tech Stack

### Backend
- **[Litestar][litestar]** - High-performance ASGI framework for modern Python web apps.
- **[PostgreSQL][postgresql]** - Robust relational database for data storage.
- **[Piccolo][piccolo]** - Async ORM and query builder with migration support.

### Frontend
- **[Next.js][nextjs]** - React framework for production-ready applications
- **[TypeScript][typescript]** - Static typing for improved development experience
- **[Tailwind CSS][tailwind]** - Utility-first CSS framework for rapid UI development
- **[Chart.js][chartjs]** - Simple yet flexible JavaScript charting library

## Getting Started

### Prerequisites

The easiest way to get the required Docker environment is by installing **[Docker Desktop][docker-desktop]**, which includes both Docker Engine and Docker Compose.

Alternatively, if you install the components separately:
- **Docker Engine:** Version 28 or later. [Install Docker Engine](https://docs.docker.com/engine/install/)
- **Docker Compose:** Version 2 (V2) or later. If you installed Docker Engine separately, you might need to [install the Compose plugin](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually).

You can verify your installation by running:
```bash
docker --version
docker compose version
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

1. Build and start all services (backend, frontend, and database):
   ```bash
   docker compose up --build
   ```

2. The services will be available at:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Piccolo admin UI: http://localhost:8000/admin/

3. To stop and remove containers:
   ```bash
   docker compose down
   ```

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
[tailwind]: https://tailwindcss.com/
[typescript]: https://www.typescriptlang.org/

# Freya

A modern financial application to track spending, organize transactions, and visualize financial trends.

## Tech Stack

### Backend
- **[Litestar][litestar]** - High-performance ASGI framework for modern Python web apps.
- **[PostgreSQL][postgresql]** - Robust relational database for data storage.
- **[Piccolo][piccolo]** - Async ORM and query builder with migration support.

### Frontend
- **Next.js** - React framework for production-ready applications
- **TypeScript** - Static typing for improved development experience
- **Tailwind CSS** - Utility-first CSS framework for rapid UI development
- **Chart.js** - Simple yet flexible JavaScript charting library

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

### Backend Setup

Docker Compose is used to orchestrate the backend service and its database.

1. Copy the example environment files, then **edit `/.env` and `backend/.env`** to set your necessary secrets and configuration:
   ```bash
   cp .env.example .env
   cp backend/.env.example backend/.env
   ```

2. Build and start services:
   ```bash
   docker compose up --build
   ```
3. The backend API will be available at http://localhost:8000, and the Piccolo admin UI at http://localhost:8000/admin/.

4. To stop and remove containers:
   ```bash
   docker compose down
   ```

### Frontend Setup

1. Copy the example environment file and update if needed:
   ```bash
   cp frontend/.env.example frontend/.env.local
   ```

2. Install dependencies:
   ```bash
   cd frontend
   npm install
   # or
   pnpm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   # or
   pnpm dev
   ```

4. The frontend application will be available at http://localhost:3000.

## Deployment
...

## License
MIT


[docker-desktop]: https://www.docker.com/products/docker-desktop/
[litestar]: https://litestar.dev/
[piccolo]: https://piccolo-orm.com/
[postgresql]: https://www.postgresql.org/

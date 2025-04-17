FROM node:22

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@latest --activate
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install
COPY . .

CMD ["pnpm", "run", "dev", "--hostname", "0.0.0.0"]

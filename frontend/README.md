# Freya Frontend

This service is containerized via Docker Compose. See the [project root README](../README.md) for setup and running instructions.

## Access Frontend

- Frontend Application: http://localhost:3000

## Linting & Formatting

This project uses [Biome][] for code linting and formatting.

#### Check and Fix (Safe)
Run `biome` check and automatically fix safe violations.

```bash
pnpm run check:biome
```

#### Check and Fix (Unsafe)
Run `biome` check and apply potentially unsafe fixes.

```bash
pnpm run check:biome:unsafe
```

#### Format
Run `biome` formatter and write changes.

```bash
pnpm run format:biome
```

#### ESLint

This project also uses [ESLint][] for additional linting via Next.js integration.

```bash
pnpm run lint:next
```

[Biome]: https://biomejs.dev/
[ESLint]: https://eslint.org/

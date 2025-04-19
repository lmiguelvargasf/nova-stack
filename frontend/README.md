# Freya Frontend

This service is containerized via Docker Compose. See the [project root README](../README.md) for setup and running instructions.

## Access Frontend

- Frontend Application: http://localhost:3000

## Linting & Formatting

This project uses [Biome][] for code linting and formatting.

#### Check and Apply Safe Fixes
Find violations and automatically apply safe fixes (including formatting).

```bash
pnpm run check:biome
```

#### Check and Apply All Fixes (Potentially Unsafe)
Find violations and apply all available fixes (including potentially unsafe ones and formatting).

```bash
pnpm run check:biome:unsafe
```

#### Format Code
Format the codebase using Biome.

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

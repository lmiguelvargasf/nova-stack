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

## Testing

This project uses [Vitest][] for testing.

#### Run Tests (Watch Mode)
Run tests and watch for file changes:
```bash
pnpm run test
```

#### Run Tests with UI
Run tests with an interactive UI ([Vitest UI][]):
```bash
pnpm run test:ui
```
*Note: after running the command, access the UI at [Vitest UI Localhost][].*

#### Run All Tests Once
Execute the full test suite once:
```bash
pnpm run test:run
```

#### Generate Coverage Report
Run all tests and generate a coverage report:
```bash
pnpm run coverage
```
 
## End-to-End (E2E) Testing

This project uses [Playwright][] for end-to-end testing. Tests are located in the `e2e` directory.

#### Run E2E Tests (Headless)
Run all Playwright tests in headless mode:
```bash
pnpm run test:e2e
```

#### Run E2E Tests with Playwright Test UI
Run tests with the interactive Playwright Test UI:
```bash
pnpm run test:e2e:ui
```
*Note: After starting, access the UI at http://localhost:9323/ by default.*

#### Show Playwright HTML Report
After running tests, view the HTML report with:
```bash
pnpm run test:e2e:report
```

[Biome]: https://biomejs.dev/
[ESLint]: https://eslint.org/
[Playwright]: https://playwright.dev/
[Vitest]: https://vitest.dev/
[Vitest UI]: https://vitest.dev/guide/ui
[Vitest UI Localhost]: http://localhost:51204/__vitest__/

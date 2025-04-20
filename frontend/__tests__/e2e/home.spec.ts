import { test, expect } from '@playwright/test';

test.describe('Home Page', () => {
  test('should load and display main elements', async ({ page }) => {
    // Navigate to application root
    await page.goto('http://localhost:3000');

    // Expect the page to have the correct title
    await expect(page).toHaveTitle('Create Next App');

    // Expect the Next.js logo to be visible
    const logo = page.getByRole('img', { name: 'Next.js logo' });
    await expect(logo).toBeVisible();

    // Expect the 'Get started by editing' instruction to be visible
    await expect(
      page.getByText(/Get started by editing/),
    ).toBeVisible();
  });
});
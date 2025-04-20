import { render, screen } from "@testing-library/react";
import { expect, test } from "vitest";

import Home from "@/app/page";

test("renders get started text", () => {
  render(<Home />);
  expect(screen.getByText(/Get started by editing/i)).toBeInTheDocument();
});

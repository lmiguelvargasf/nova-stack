import React from "react";
import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";

import Home from "@/app/page";

test("renders get started text", () => {
  render(<Home />);
  expect(screen.getByText(/Get started by editing/i)).toBeInTheDocument();
});

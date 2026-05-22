import { render, screen, waitFor } from "@testing-library/react";

import App from "./App";

let mockPathname = "/home";
jest.mock(
  "react-router-dom",
  () => ({
    Navigate: ({ to }) => <div>NAVIGATE:{to}</div>,
    Route: ({ element }) => <>{element}</>,
    Routes: ({ children }) => <>{children}</>,
    useLocation: () => ({ pathname: mockPathname }),
  }),
  { virtual: true }
);

jest.mock("../api/axiosInstance", () => ({
  __esModule: true,
  default: { get: jest.fn() },
}));

jest.mock("../Components/Header", () => () => <div data-testid="header">Header</div>);

jest.mock("../Pages", () => ({
  HomePage: () => <div>Home</div>,
  ProfilePage: () => <div>Profile</div>,
  GamePage: () => <div>Game</div>,
  CatalogPage: () => <div>Catalog</div>,
  LoginPage: () => <div>Login</div>,
  RegisterPage: () => <div>Register</div>,
}));

describe("App routes", () => {
  afterEach(() => {
    localStorage.clear();
    mockPathname = "/home";
  });

  it("redirects to login when profile route is opened without token", async () => {
    mockPathname = "/profile";
    render(<App />);

    expect(await screen.findByText("NAVIGATE:/login")).toBeInTheDocument();
  });

  it("drops expired session and redirects from profile to login", async () => {
    const axiosInstance = require("../api/axiosInstance").default;
    axiosInstance.get.mockRejectedValueOnce(new Error("401"));
    localStorage.setItem("accessToken", "expired-token");
    mockPathname = "/profile";

    render(<App />);

    await waitFor(() => {
      expect(localStorage.getItem("accessToken")).toBeNull();
    });
    expect(await screen.findByText("NAVIGATE:/login")).toBeInTheDocument();
  });
});

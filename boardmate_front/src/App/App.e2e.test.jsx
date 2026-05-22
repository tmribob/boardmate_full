import { render, screen } from "@testing-library/react";

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

jest.mock("../Components/Header", () => () => <div>Header</div>);

jest.mock("../Pages", () => ({
  HomePage: () => <div>Home</div>,
  ProfilePage: () => <div>Profile</div>,
  GamePage: () => <div>Game</div>,
  CatalogPage: () => <div>Catalog</div>,
  LoginPage: () => <div>Login</div>,
  RegisterPage: () => <div>Register</div>,
}));

describe("E2E basic flow", () => {
  afterEach(() => {
    localStorage.clear();
    mockPathname = "/home";
  });

  it("opens profile and sends guest to login", async () => {
    mockPathname = "/profile";
    render(<App />);

    expect(await screen.findByText("NAVIGATE:/login")).toBeInTheDocument();
  });
});

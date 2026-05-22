import authService from "./AuthService";

jest.mock("./axiosInstance", () => ({
  __esModule: true,
  default: {
    post: jest.fn(),
  },
}));

describe("AuthService", () => {
  afterEach(() => {
    localStorage.clear();
  });

  it("converts credentials to OAuth2 fields", () => {
    const payload = authService.convertToOAuth2Form({
      email: "user@mail.com",
      password: "123456",
    });

    expect(payload).toEqual({
      username: "user@mail.com",
      password: "123456",
      grant_type: "password",
      scope: "read write",
    });
  });

  it("reports authentication state from localStorage", () => {
    expect(authService.isAuthenticated()).toBe(false);
    localStorage.setItem("accessToken", "token");
    expect(authService.isAuthenticated()).toBe(true);
  });
});

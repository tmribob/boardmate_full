import axiosInstance from './axiosInstance';

class AuthService {

  convertToOAuth2Form(credentials) {
    return {
      username: credentials.email,
      password: credentials.password,
      grant_type: 'password',
      scope: 'read write'
    };
  }

  async login(credentials) {

    const formData = this.convertToOAuth2Form(credentials);

    const params = new URLSearchParams();

    params.append('username', formData.username);
    params.append('password', formData.password);

    if (formData.scope) {
      params.append('scope', formData.scope);
    }

    if (formData.grant_type) {
      params.append('grant_type', formData.grant_type);
    }

    const response = await axiosInstance.post(
      '/auth/login',
      params,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    );
    if (response.data.access_token) {
      localStorage.setItem('accessToken', response.data.access_token);
    }

    return response.data;
  }

  async register(userData) {
    console.log(userData)
    await axiosInstance.post(
      '/auth/register',
      userData
    );
  }

  async logout() {
    try {
      await axiosInstance.post("/auth/logout")
    } catch (error) {
      console.error(error)
    } finally {
      localStorage.removeItem('accessToken');
      window.location.href = "/home"
    }
  }

  isAuthenticated() {
    return !!localStorage.getItem('accessToken');
  }
}

const authService = new AuthService();

export default authService;
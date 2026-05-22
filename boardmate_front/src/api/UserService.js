import axiosInstance from './axiosInstance';

class UserService {
  async getRecommendateFriends() {
    const response = await axiosInstance.get('/friends/');
    return response.data.map((user) => ({
      ...user,
      id: user.uuid,
      avatar: user.avatar || "/avatar.png"
    }));
  }
}

const userService = new UserService();

export default userService;
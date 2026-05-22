import {Navigate, Route, Routes, useLocation} from "react-router-dom";
import {useEffect, useState} from "react";

import Header from "../Components/Header";
import {
  HomePage, ProfilePage, GamePage, CatalogPage, LoginPage, RegisterPage
} from "../Pages"
import axiosInstance from "../api/axiosInstance";

const App = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);

  const location = useLocation();
  const hideHeader = ['/login', '/register'].includes(location.pathname);

  useEffect(() => {
    const loadProfile = async () => {
      const token = localStorage.getItem("accessToken");

      if (!token) {
        setLoading(false);
        return;
      }

      try {
        const [userRes, friendsRes] = await Promise.all([
          axiosInstance.get("/users/"),
          axiosInstance.get("/friends/")
        ]);
        const user = userRes.data;
        const friends = friendsRes.data || [];

        setProfile({
          avatar: user.avatar || "/avatar.png",
          id: user.uuid,
          nickname: user.nickname,
          friends: friends.map((friend) => ({
            ...friend,
            id: friend.uuid,
            avatar: friend.avatar || "/avatar.png"
          })),
          description: user.description || "",
        });
      } catch (e) {
        localStorage.removeItem("accessToken");
        setProfile(null);
      } finally {
        setLoading(false);
      }
    };
    loadProfile();
  }, []);

  if (loading && location.pathname === '/profile') {
    return <></>;
  }

  if (!profile && location.pathname === '/profile') {
    return <Navigate to="/login" replace />;
  }

  return (<>
    {!hideHeader && <Header avatar={profile?.avatar} />}
    <Routes>
      <Route
        path="*"
        element={<Navigate
          to="/home"
          replace
        />}
      />
      <Route
        path="/catalog"
        element={<CatalogPage />}
      />
      <Route
        path="/game/:id"
        element={<GamePage />}
      />
      <Route
        path="/home"
        element={<HomePage />}
      />
      <Route
        path={'/login'}
        element={<LoginPage />}
      />
      <Route
        path={'/register'}
        element={<RegisterPage />}
      />
      <Route
        path={'/profile'}
        element={<ProfilePage
          profile={profile}
        />}
      />
    </Routes>
  </>);
}

export default App;

import style from './HomePage.module.css';
import {useEffect, useState} from "react";
import games from "../../data/games";
import GameCard from "../../Components/GameCard";
import Pagination from "../../Components/Catalog/Pagination";
import Button from "../../Components/Button";
import authService from "../../api/AuthService";
import userService from "../../api/UserService";

const HomePage = () => {
  const [currentGame, setCurrentGame] = useState(0);
  const [currentFriend, setCurrenFriend] = useState(0);
  const [friends, setFriends] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getFriends = async () => {
      try {
        const res = await userService.getRecommendateFriends();
        setFriends(res);
      } catch (error) {
        setFriends([]);
      } finally {
        setLoading(false);
      }
    }
    getFriends();
  }, []);


  if (!authService.isAuthenticated() || loading) {
    return <></>
  }

  return (<main className={style.main}>
    <h1 className={style.title}>Рекомендованные игры и друзья</h1>
    <div className={style.recommendation}>
      <div className={style.carousel}>
        <GameCard game={games[currentGame]} />
        <Pagination
          currentPage={currentGame}
          isView={false}
          setCurrentPage={setCurrentGame}
          cyclically={true}
          maxPage={games.length}
        />
      </div>
      {friends.length > 0 &&
        <div className={style.carousel}>
          <div className={style.friend}>
            <img
              src={friends[currentFriend].avatar}
              alt={friends[currentFriend].nickname}
              className={style.avatar}
            />
            <h1> {friends[currentFriend].nickname}</h1>
            <Button
              content="Добавить"
              theme="green"
              width="50%"
            />
          </div>
          <Pagination
            currentPage={currentFriend}
            isView={false}
            setCurrentPage={setCurrenFriend}
            cyclically={true}
            maxPage={friends.length}
          />
        </div>}
    </div>
  </main>);
};

export default HomePage;
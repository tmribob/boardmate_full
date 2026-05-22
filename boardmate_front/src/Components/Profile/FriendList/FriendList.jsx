import style from './FriendList.module.css';
import {useState} from "react";
import Button from "../../Button";

const getFriendsWord = (count) => {
  count = Math.abs(count);
  const lastTwo = count % 100;
  if (lastTwo >= 11 && lastTwo <= 14) return 'друзей';
  const last = count % 10;
  if (last === 1) return 'друг';
  if (last >= 2 && last <= 4) return 'друга';
  return 'друзей';
};

const FriendList = ({friends}) => {

  const [isAllFriends, setAllFriends] = useState(false);
  const changeAllFriends = () => {
    setAllFriends((prev) => !prev);
  }

  const visibleFriends = friends ? (isAllFriends ? friends : friends.slice(0, 10)) : [];

  return (<div className={style.friends}>
    {friends && <>
      <div className={style.headerFriends}>
        <h1 className={style.titleFriends}>Друзья</h1>
        <span className={style.numberOfFriends}>
        {friends.length} {getFriendsWord(friends.length)}
      </span>
      </div>
      <div className={style.friendsList}>
        {visibleFriends.map((v) => (<div
          className={style.friendCard}
          key={v.id || v.uuid}
        >
          <img
            src={v.avatar}
            alt="avatar"
            className={style.avatar}
          />
          <span className={style.nickname}>{v.nickname}</span>
        </div>))}
        {friends.length > 10 && <Button
          content={isAllFriends ? "скрыть" : "показать всех"}
          onClick={changeAllFriends}
        />}
      </div>
    </>}
  </div>);
};

export default FriendList;
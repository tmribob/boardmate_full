import style from './ProfilePage.module.css';
import ProfileCard from "../../Components/Profile/ProfileCard";
import FriendList from "../../Components/Profile/FriendList";


const ProfilePage = ({profile}) => {
  return (<main className={style.main}>
      <ProfileCard
        nickname={profile.nickname}
        imgSrc={profile.avatar}
        description={profile.description}
      />
      <FriendList
        friends={profile?.friends}
      />
    </main>
  );
};

export default ProfilePage;
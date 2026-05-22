import style from './ProfileCard.module.css';
import Button from "../../Button";
import {MdEdit} from "react-icons/md";
import authService from "../../../api/AuthService";
import {useNavigate} from "react-router-dom";

const ProfileCard = ({imgSrc, nickname, description}) => {
  const navigate = useNavigate();
  const exit = () => {
    authService.logout();
    navigate("/home")
  }

  return (<div className={style.profile}>
    <img
      src={imgSrc}
      alt="avatar"
      className={style.avatar}
    />
    <div className={style.profileInfo}>
      <h1 className={style.nickname}>{nickname}</h1>
      <span className={style.description}>{description}</span>
      <div className={style.actions}>
        <Button
          content={"Редактировать"}
          theme="green"
          width="60%"
        />
        <Button
          content={"Выйти"}
          theme="yellow"
          width="35%"
          onClick={exit}
        />
      </div>
    </div>
  </div>);
};

export default ProfileCard;
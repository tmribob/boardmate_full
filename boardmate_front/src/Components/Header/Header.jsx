import style from './Header.module.css';
import Logo from "./Logo";
import {NavLink} from "react-router-dom";
import Button from "../Button";
import NavBar from "./NavBar";
import authService from "../../api/AuthService";

const Header = ({avatar}) => {

  return (<div className={style.header}>
    <div className={style.headerContainer}>
      <Logo />
      <NavBar />
    </div>
    <div className={style.headerContainer}>
      {authService.isAuthenticated() ?
        <NavLink to="/profile">
          <img
            className={style.avatar}
            src={avatar}
            alt="profile"
          />
        </NavLink>
        :
        <NavLink to="/login">
          <Button
            theme="green"
            content="Войти"
          />
        </NavLink>}
    </div>
  </div>);
};

export default Header;
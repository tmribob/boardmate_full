import style from './Logo.module.css'
import {NavLink} from "react-router-dom";

const Logo = () => {
  return (
    <NavLink
      to="/home"
      className={style.logo}
    >
      <img
        src="./logo.svg"
        alt="Лого"
        className={style.logoSVG}
      />
      <h1 className={style.siteName}>GameHub</h1>
    </NavLink>
  );
};

export default Logo;
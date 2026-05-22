import style from './NavBar.module.css';
import {NavLink} from "react-router-dom";

const NavBar = () => {
  return (<>
    <NavLink
      to="/catalog"
      className={style.navElement}
    >
      Каталог
    </NavLink>
  </>);
};

export default NavBar;
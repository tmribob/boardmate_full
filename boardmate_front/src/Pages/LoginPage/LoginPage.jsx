import style from './LoginPage.module.css';
import {MdAlternateEmail} from "react-icons/md";
import {IoKeyOutline} from "react-icons/io5";
import {useState} from "react";
import Button from "../../Components/Button";
import authService from "../../api/AuthService";

import {NavLink, useNavigate} from "react-router-dom";
import InputField from "../../Components/InputField";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleEmail = (value) => {
    setEmail(value)
  }

  const handlePassword = (value) => {
    setPassword(value)
  }

  const login = async () => {
    if (password) {
      await authService.login({email,password});
      navigate("/")
    }
  }

  return (<main className={style.main}>
    <form className={style.contain}>
      <h1 className={style.title}>Авторизация</h1>
      <div className={style.inputs}>
        <InputField
          name="email"
          icon={MdAlternateEmail}
          onChange={handleEmail}
          label="Электронная почта"
          inputValue={email}
          placeholder="Введите email"
        />
        <InputField
          name="password"
          icon={IoKeyOutline}
          onChange={handlePassword}
          label="Пароль"
          inputValue={password}
          placeholder="Введите пароль"
        />
        <NavLink
          to="/register"
          className={style.register}
        >нет аккаунта, зарегестрируйся</NavLink>
      </div>
      <div className={style.action}>
        <Button
          content="На главную"
          onClick={() => navigate("/")}
          theme="grey"
        />
        <Button
          content="Войти"
          theme="yellow"
          onClick={login}
        />
      </div>
    </form>
  </main>);
};

export default LoginPage;
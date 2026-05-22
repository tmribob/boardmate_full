import style from './RegisterPage.module.css';
import InputField from "../../Components/InputField";
import {MdAlternateEmail} from "react-icons/md";
import {IoKeyOutline} from "react-icons/io5";
import {MdOutlinePerson} from "react-icons/md";
import Button from "../../Components/Button";
import {NavLink, useNavigate} from "react-router-dom";
import {useState} from "react";
import authService from "../../api/AuthService";

const RegisterPage = () => {
  const [email, setEmail] = useState("");
  const [nickname, setNickname] = useState("");
  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");
  const navigate = useNavigate();

  const handleEmail = (value) => {
    setEmail(value)
  }

  const handleNickname = (value) => {
    setNickname(value)
  }

  const handlePassword1 = (value) => {
    setPassword1(value)
  }
  const handlePassword2 = (value) => {
    setPassword2(value)
  }

  const register = async () => {
    if (email && nickname && password1 && password2 && (password1 === password2)) {
      console.log(email, nickname, password2, password1)
      await authService.register({
        email,
        nickname: nickname,
        password: password2
      })
      console.log("fds")
      navigate("/login")
    }
  }


  return (<main className={style.main}>
    <form className={style.contain}>
      <h1 className={style.title}>Регистрация</h1>
      <div className={style.inputs}>
        <InputField
          name="nickname"
          icon={MdOutlinePerson}
          onChange={handleNickname}
          label="Имя пользователя"
          inputValue={nickname}
          placeholder="Введите nickname"
        />
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
          onChange={handlePassword1}
          label="Пароль"
          inputValue={password1}
          placeholder="Введите пароль"
        />
        <InputField
          name="password"
          icon={IoKeyOutline}
          onChange={handlePassword2}
          label="Повторите Пароль"
          inputValue={password2}
          placeholder="Введите пароль снова"
        />
        <NavLink
          to="/login"
          className={style.login}
        >уже есть аккаунт, войди</NavLink>
      </div>
      <div className={style.action}>
        <Button
          content="На главную"
          onClick={() => navigate("/")}
          theme="grey"
        />
        <Button
          content="Зарегестрироваться"
          theme="yellow"
          onClick={register}
        />
      </div>
    </form>
  </main>);
};

export default RegisterPage;
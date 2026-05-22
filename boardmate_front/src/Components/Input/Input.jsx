import style from './Input.module.css';

const Input = ({
                 name,
                 value,
                 onChange,
                 type = "text",
                 placeHolder,
                 icon: Icon = null
               }) => {
  return (<div className={style.area}>
    {Icon && <Icon className={style.icon} />}
    <input
      type={type}
      name={name}
      className={style.input}
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeHolder}
      autoComplete={name === "search" ? "off" : "on"}
    />
  </div>);
};

export default Input;
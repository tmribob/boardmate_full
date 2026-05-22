import style from './InputField.module.css';
import Input from "../Input";

const InputField = ({
                      name,
                      label,
                      icon,
                      inputValue: value,
                      placeholder,
                      onChange,
                    }) => {
  return (<div className={style.field}>
    <label
      htmlFor={name}
      className={style.label}
    >{label}
    </label>
    <Input
      name={name}
      icon={icon}
      value={value}
      placeHolder={placeholder}
      onChange={onChange}
    />
  </div>);
};

export default InputField;
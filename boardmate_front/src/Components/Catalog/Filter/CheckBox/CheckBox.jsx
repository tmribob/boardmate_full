import style from './CheckBox.module.css';

const CheckBox = ({name, label, onChange, checked,id}) => {
  return (<label
    htmlFor={name}
    className={style.checkBox}
  >
    <input
      type="checkbox"
      name={name}
      id={name}
      onChange={() => onChange(id)}
      checked={checked}
    />
    {label}</label>);
};

export default CheckBox;
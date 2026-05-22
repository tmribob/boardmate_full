import style from './CheckBoxArea.module.css';
import CheckBox from "../CheckBox";

const CheckBoxArea = ({array, onChange}) => {
  return (<div className={style.checkBoxArea}>
    {array && array.map((v) => (
      <CheckBox
        key={v.id}
        id={v.id}
        name={v.name}
        label={v.label}
        checked={v.status}
        onChange={onChange}
      />))}
  </div>);
};

export default CheckBoxArea;
import style from './RangeInput.module.css';

const RangeInput = ({name, min, max, step, value, change, isTime = false}) => {
  const newMax = isTime ? `${max / 60}+ ч` : `${max}+`;
  const newMin = `${min}${isTime ? " мин" : ""}`;
  const hours = Math.floor(value / 60) ? `${Math.floor(value / 60)} ч ` : "";
  const minutes = value % 60 ? `${value % 60} мин` : "";
  const currentValue = isTime ? `${hours}${minutes}` : `${value}`;
  const percentProgressBar = (value - min) / (max - min)

  return (<div className={style.rangeDiv}>
    <input
      className={`${style.rangeBar} rangeBarGlobal`}
      id={name}
      type="range"
      min={min}
      max={max}
      step={step}
      value={value}
      onChange={(e) => change(e.target.value)}
    />
    <div
      className={style.progressBar}
      style={{width: `calc(${percentProgressBar * 100}% - ${Math.floor(percentProgressBar * 24)}px)`}}
    ></div>
    <div className={style.description}>
      <p className={style.min}>{newMin}</p>
      <p className={style.currentValue}>{currentValue}</p>
      <p className={style.max}>{newMax}</p>
    </div>
  </div>);
};

export default RangeInput;
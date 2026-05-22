import style from './StarList.module.css';
import {CiStar} from "react-icons/ci";
import {FaStar} from "react-icons/fa";


const StarList = ({rate, changeRate}) => {
  return (<div className={style.starList}>
    {[1, 2, 3, 4, 5].map((v) => (v > rate ? < CiStar
        className={style.star}
        onClick={changeRate && (() => changeRate(v))}
        key={v}
      /> :
      <FaStar
        className={style.star}
        onClick={changeRate && (() => changeRate(v))}
        key={v}
      />))}
  </div>);
};

export default StarList;
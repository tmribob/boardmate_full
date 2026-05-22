import style from './GameCard.module.css';
import StarList from "../StarList";
import Button from "../Button";
import {FaBrain, FaClock, FaHeart} from "react-icons/fa6";
import {IoPeople} from "react-icons/io5";
import {FaRegHeart} from "react-icons/fa";
import difficultiesList from "../../data/difficultiesList";
import genresList from "../../data/genresList";
import {useNavigate} from "react-router-dom";

const GameCard = ({game}) => {
  const navigate = useNavigate();
  const goToGame =()=>{
    navigate(`/game/${game.id}`);
  };

  return (<div className={style.card}>
    <img
      src={game.imgSrc}
      alt={game.name}
      className={style.imgGame}
    />
    <h1 className={style.nameGame}>
      {game.name}
    </h1>
    <div className={style.character}>
      {genresList.filter((v) =>
        game.genres.includes(v.id)).map((v) =>
        <p className={style.genreGame} key={v.label}>{v.label}</p>)}
    </div>
    <div className={style.character}>
      <StarList rate={game.rate} />
      {game.rate}
    </div>
    <div className={style.character}>
      <FaBrain />
      {difficultiesList.filter((v) =>
        v.id === game.difficulty).map((v) =>
        <p className={style.difficultyGame} key={v.label}>{v.label}</p>)}
    </div>
    <div className={style.character}>
      <FaClock />
      {game.duration.min}-{game.duration.max} мин
    </div>
    <div className={style.character}>
      <IoPeople />
      {game.numberPeople.min}-{game.numberPeople.max} игроков
    </div>
    <div className={style.character}>
      <FaHeart />
      {game.followers} любителей
    </div>
    <div className={style.activityGame}>
      <Button
        theme="green"
        content="Подробнее"
        onClick={goToGame}
      />
      <FaRegHeart className={style.likeGame}/>
    </div>
  </div>);
};

export default GameCard;
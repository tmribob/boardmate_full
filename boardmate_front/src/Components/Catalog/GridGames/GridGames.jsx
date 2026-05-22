import style from './GridGames.module.css';
import GameCard from "../../GameCard";

const GridGames = ({games}) => {
  return (<div className={style.gridGames}>
    {games && games.map((v) => (<GameCard game={v} key={v.id}/>))}
  </div>);
};

export default GridGames;
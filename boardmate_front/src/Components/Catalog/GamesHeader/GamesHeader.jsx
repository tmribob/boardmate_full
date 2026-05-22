import style from './GamesHeader.module.css';

const GamesHeader = ({gamesCount, sort, onSortChange}) => {
  const getGamesWord = (count) => {
    count = count % 100;
    const n = count % 10;

    if (n > 1 && n < 5) return 'игры';
    if (n === 1) return 'игра';
    return 'игр';
  };
  return (<div className={style.gamesHeader}>
      <div className={style.resultsInfo}>
        <h1 className={style.catalogTitle}>Каталог игр</h1>
        <p className={style.gamesCount}>Найдено {gamesCount} {getGamesWord(gamesCount)}</p>
      </div>

      <div className={style.sorting}>
        <label className={style.sortBy}>Сортировка по:</label>
        <select
          className={style.sortSelection}
          value={sort}
          onChange={(e) => onSortChange(e.target.value)}
        >
          <option value="popularity">Популярности</option>
          <option value="rating">Рейтингу</option>
        </select>
      </div>
    </div>
  );
}

export default GamesHeader;
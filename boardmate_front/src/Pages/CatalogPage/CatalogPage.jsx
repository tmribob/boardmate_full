import style from './CatalogPage.module.css';
import Filter from '../../Components/Catalog/Filter'
import {useState} from "react";
import GamesHeader from "../../Components/Catalog/GamesHeader";
import GridGames from "../../Components/Catalog/GridGames";
import Pagination from "../../Components/Catalog/Pagination";

import gamesStart from "./../../data/games"

const CatalogPage = () => {
  const [sort, setSort] = useState("popularity")
  const onSortChange = (v) => {
    setSort(v);
  }
  const [currentPage, setCurrentPage] = useState(1);
  const maxPage = Math.ceil(gamesStart.length / 6);
  return (<main className={style.main}>
    <Filter />
    <div className={style.catalog}>
      <GamesHeader
        gamesCount={gamesStart.length}
        sort={sort}
        onSortChange={onSortChange}
      />
      <GridGames
        games={gamesStart.filter((_, i) =>
          Math.floor(i / 6) + 1 === currentPage)}
      />
      <Pagination
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        maxPage={maxPage}
      />
    </div>
  </main>);
};

export default CatalogPage;
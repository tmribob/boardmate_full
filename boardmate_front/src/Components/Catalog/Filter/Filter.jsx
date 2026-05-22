import style from './Filter.module.css';
import {useState} from "react";

import CheckBoxArea from "./CheckBoxArea";
import RangeInput from "./RangeInput";

import StarList from "../../StarList";
import genresList from "../../../data/genresList";
import difficultiesList from "../../../data/difficultiesList";
import Button from "../../Button";

const Filter = () => {
  const [genres, setGenres] = useState(genresList || []);
  const [difficulties, setDifficulties] = useState(difficultiesList || []);
  const [numberPeople, setNumberPeople] = useState(4);
  const [duration, setDuration] = useState(15);
  const [rate, setRate] = useState(0)

  const changeNumberPeople = (v) => {
    setNumberPeople(Number(v));
  };

  const changeDuration = (v) => {
    setDuration(Number(v));
  };

  const changeRate = (id) => {
    setRate(id);
  };

  const changeGenres = (id) => {
    setGenres((array) => array.map((v) => v.id === id ? {
      ...v, status: !v.status
    } : v));
  };

  const changeDifficulties = (id) => {
    setDifficulties((array) => array.map((v) => v.id === id ? {
      ...v, status: !v.status
    } : v));
  };

  const apply = () => {
    //BACK
  };

  const reset = () => {
    setGenres((array) => array.map((v) => ({
      ...v, status: false
    })));
    setDifficulties((array) => array.map((v) => ({
      ...v, status: false
    })));
    setDuration(15);
    setNumberPeople(4);
    setRate(0);
  };

  return (<form className={style.formFilter}>
    <h3 className={style.title}> Фильтры</h3>
    <label
      className={style.titleCategories}
    >Жанр
    </label>
    <CheckBoxArea
      array={genres}
      onChange={changeGenres}
    />
    <label
      className={style.titleCategories}
    >Сложность
    </label>
    <CheckBoxArea
      array={difficulties}
      onChange={changeDifficulties}
    />
    <label
      className={style.titleCategories}
    >Колличество игроков
    </label>
    <RangeInput
      name="number_people"
      max={8}
      min={1}
      step={1}
      value={numberPeople}
      change={changeNumberPeople}
    />
    <label
      className={style.titleCategories}
    >Длительность партии
    </label>
    <RangeInput
      name="duration"
      max={180}
      min={15}
      step={15}
      value={duration}
      change={changeDuration}
      isTime={true}
    />
    <label
      className={style.titleCategories}
    >Минимальный рейтинг
    </label>
    <StarList rate={rate} changeRate={changeRate}/>
    <Button
      content="Применить"
      theme="yellow"
      onClick={apply}
      width="70%"
      type="submit"
    />
    <Button
      content="Сбросить"
      theme="grey"
      onClick={reset}
      width="70%"
    />
  </form>);
};

export default Filter;
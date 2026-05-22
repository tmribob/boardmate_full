import style from './GamePage.module.css';
import {useParams} from "react-router-dom";

const GamePage = () => {
  const {id} = useParams()
  return (
    <>
      {id}
    </>
  );
};

export default GamePage;
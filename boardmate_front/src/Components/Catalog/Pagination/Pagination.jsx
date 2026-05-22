import style from './Pagination.module.css';
import Button from "../../Button";

const Pagination = ({
                      currentPage,
                      setCurrentPage,
                      maxPage,
                      isView = true,
                      cyclically = false
                    }) => {
  const changePage = (v) => {
    if (cyclically) {
      setCurrentPage(v)
    } else if (1 <= v && v <= maxPage) {
      setCurrentPage(v);
    }
  };
  const nextPage = () => {
    if (cyclically) {
      setCurrentPage(prev => (prev + 1) % maxPage);
    } else if (currentPage < maxPage) {
      setCurrentPage(prev => prev + 1);
    }
  };
  const prevPage = () => {
    if (cyclically) {
      setCurrentPage(prev => (maxPage + prev - 1) % maxPage);
    } else if (currentPage > 1) {
      setCurrentPage(prev => prev - 1);
    }
  };
  const renderPages = () => {
    if (maxPage <= 5) {
      return Array.from({length: maxPage}, (_, i) => (<Button
        key={i + 1}
        width="5em"
        content={i + 1}
        onClick={() => changePage(i + 1)}
        theme={(i + 1) === currentPage ? "green" : "transparent"}
      />))
    }
    const pages = [1];

    if (currentPage <= 3) {
      for (let i = 2; i <= currentPage + 1; i++) pages.push(i);
      pages.push(0, maxPage);
    } else {
      pages.push(0);
      const start = Math.max(currentPage - 1, maxPage - 3);
      const end = Math.min(currentPage + 1, maxPage);
      for (let i = start; i <= end; i++) pages.push(i);
      if (end < maxPage) pages.push(0, maxPage);
    }
    return pages.map((number, index) => {
      if (number) {
        return <Button
          key={number}
          width="5em"
          content={number}
          onClick={() => changePage(number)}
          theme={number === currentPage ? "green" : "transparent"}
        />
      } else {
        return <span key={`dots${index}`}>...</span>
      }
    });
  }

  return (<div className={style.pagesList}>
    {(cyclically || currentPage !== 1) && <Button
      content="<"
      width="5em"
      onClick={prevPage}
    />}
    {isView && renderPages()}
    {(cyclically || currentPage !== maxPage) && <Button
      content=">"
      width="5em"
      onClick={nextPage}
    />}

  </div>);
};

export default Pagination;
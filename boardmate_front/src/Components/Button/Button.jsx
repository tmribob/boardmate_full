import style from './Button.module.css';

const Button = ({
                  onClick,
                  content,
                  type = "button",
                  theme = "transparent",
                  title = "",
                  width = "100%",
                  height = "2.2em",
                  fontSize = "1.1em"
                }) => {
  return (<div style={{width: width, height: height, fontSize: fontSize}}>
    < button
      type={type}
      className={`${style.button} ${style[theme]}`}
      onClick={onClick}
      title={!!title ? content : title}
    >
      {content}
    </button>
  </div>);
};

export default Button;
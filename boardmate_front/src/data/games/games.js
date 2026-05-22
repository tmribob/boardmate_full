const games = [{
  id: 0,
  name: "Каркасон",
  imgSrc: "./img.png",
  genres: [1],
  rate: 4.6,
  difficulty: 0,
  duration: {min: 30, max: 90},
  numberPeople: {min: 2, max: 5},
  followers: 12345
}, {
  id: 1,
  name: "Root",
  imgSrc: "./img.png",
  genres: [1, 2],
  rate: 4.8,
  difficulty: 2,
  duration: {min: 60, max: 120},
  numberPeople: {min: 2, max: 4},
  followers: 8567
}, {
  id: 2,
  name: "Цитадели",
  imgSrc: "./img.png",
  genres: [1, 3],
  rate: 4.4,
  difficulty: 1,
  duration: {min: 30, max: 60},
  numberPeople: {min: 2, max: 8},
  followers: 11234
}, {
  id: 3,
  name: "Колонизаторы",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.7,
  difficulty: 1,
  duration: {min: 60, max: 120},
  numberPeople: {min: 3, max: 4},
  followers: 23456
}, {
  id: 4,
  name: "Диксит",
  imgSrc: "./img.png",
  genres: [5],
  rate: 4.9,
  difficulty: 0,
  duration: {min: 30, max: 45},
  numberPeople: {min: 3, max: 6},
  followers: 18923
}, {
  id: 5,
  name: "Кодовые имена",
  imgSrc: "./img.png",
  genres: [5, 6],
  rate: 4.8,
  difficulty: 0,
  duration: {min: 15, max: 30},
  numberPeople: {min: 4, max: 8},
  followers: 16789
}, {
  id: 6,
  name: "7 Чудес",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.5,
  difficulty: 1,
  duration: {min: 30, max: 45},
  numberPeople: {min: 2, max: 7},
  followers: 14567
}, {
  id: 7,
  name: "Манчкин",
  imgSrc: "./img.png",
  genres: [7],
  rate: 4.3,
  difficulty: 0,
  duration: {min: 60, max: 120},
  numberPeople: {min: 3, max: 6},
  followers: 27890
}, {
  id: 8,
  name: "Азул",
  imgSrc: "./img.png",
  genres: [6],
  rate: 4.7,
  difficulty: 1,
  duration: {min: 30, max: 45},
  numberPeople: {min: 2, max: 4},
  followers: 9876
}, {
  id: 9,
  name: "Билет на поезд",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.6,
  difficulty: 1,
  duration: {min: 30, max: 60},
  numberPeople: {min: 2, max: 5},
  followers: 15678
}, {
  id: 10,
  name: "Тикет ту Райд: Европа",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.7,
  difficulty: 1,
  duration: {min: 30, max: 60},
  numberPeople: {min: 2, max: 5},
  followers: 20345
}, {
  id: 11,
  name: "Сплэндор",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.6,
  difficulty: 1,
  duration: {min: 30, max: 45},
  numberPeople: {min: 2, max: 4},
  followers: 17890
}, {
  id: 12,
  name: "Винодельня",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.8,
  difficulty: 2,
  duration: {min: 60, max: 90},
  numberPeople: {min: 2, max: 4},
  followers: 13456
}, {
  id: 13,
  name: "Щекины",
  imgSrc: "./img.png",
  genres: [5],
  rate: 4.5,
  difficulty: 0,
  duration: {min: 20, max: 40},
  numberPeople: {min: 4, max: 8},
  followers: 22345
}, {
  id: 14,
  name: "Один из нас",
  imgSrc: "./img.png",
  genres: [5, 6],
  rate: 4.7,
  difficulty: 0,
  duration: {min: 5, max: 15},
  numberPeople: {min: 4, max: 10},
  followers: 26789
}, {
  id: 15,
  name: "Эль Гранд Капитан",
  imgSrc: "./img.png",
  genres: [1],
  rate: 4.6,
  difficulty: 1,
  duration: {min: 45, max: 75},
  numberPeople: {min: 2, max: 5},
  followers: 14567
}, {
  id: 16,
  name: "Искры",
  imgSrc: "./img.png",
  genres: [6],
  rate: 4.9,
  difficulty: 0,
  duration: {min: 15, max: 30},
  numberPeople: {min: 2, max: 6},
  followers: 19876
}, {
  id: 17,
  name: "Каньон",
  imgSrc: "./img.png",
  genres: [1],
  rate: 4.4,
  difficulty: 1,
  duration: {min: 30, max: 60},
  numberPeople: {min: 2, max: 5},
  followers: 16789
}, {
  id: 18,
  name: "Пандемия",
  imgSrc: "./img.png",
  genres: [8],
  rate: 4.7,
  difficulty: 2,
  duration: {min: 45, max: 60},
  numberPeople: {min: 2, max: 4},
  followers: 23456
}, {
  id: 19,
  name: "Зомби",
  imgSrc: "./img.png",
  genres: [8],
  rate: 4.5,
  difficulty: 1,
  duration: {min: 45, max: 60},
  numberPeople: {min: 2, max: 6},
  followers: 18901
}, {
  id: 20,
  name: "Скайджакеры",
  imgSrc: "./img.png",
  genres: [7],
  rate: 4.6,
  difficulty: 1,
  duration: {min: 30, max: 45},
  numberPeople: {min: 3, max: 8},
  followers: 15678
}, {
  id: 21,
  name: "Кинг оф Токио",
  imgSrc: "./img.png",
  genres: [7],
  rate: 4.4,
  difficulty: 0,
  duration: {min: 30, max: 45},
  numberPeople: {min: 2, max: 6},
  followers: 20123
}, {
  id: 22,
  name: "Библиотека",
  imgSrc: "./img.png",
  genres: [6],
  rate: 4.8,
  difficulty: 1,
  duration: {min: 30, max: 60},
  numberPeople: {min: 1, max: 4},
  followers: 12390
}, {
  id: 23,
  name: "Тайный санторий",
  imgSrc: "./img.png",
  genres: [5],
  rate: 4.7,
  difficulty: 0,
  duration: {min: 20, max: 40},
  numberPeople: {min: 4, max: 12},
  followers: 23456
}, {
  id: 24,
  name: "Архитекты",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.6,
  difficulty: 1,
  duration: {min: 30, max: 60},
  numberPeople: {min: 2, max: 5},
  followers: 17654
}, {
  id: 25,
  name: "Терраформирование Марса",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.8,
  difficulty: 3,
  duration: {min: 120, max: 180},
  numberPeople: {min: 1, max: 5},
  followers: 24567
}, {
  id: 26,
  name: "Властелины Востока",
  imgSrc: "./img.png",
  genres: [1],
  rate: 4.7,
  difficulty: 2,
  duration: {min: 60, max: 120},
  numberPeople: {min: 2, max: 5},
  followers: 19876
}, {
  id: 27,
  name: "Малифум",
  imgSrc: "./img.png",
  genres: [6],
  rate: 4.9,
  difficulty: 1,
  duration: {min: 40, max: 70},
  numberPeople: {min: 2, max: 4},
  followers: 23456
}, {
  id: 28,
  name: "Остров духов",
  imgSrc: "./img.png",
  genres: [5],
  rate: 4.6,
  difficulty: 0,
  duration: {min: 30, max: 45},
  numberPeople: {min: 3, max: 6},
  followers: 16789
}, {
  id: 29,
  name: "Сопротивление",
  imgSrc: "./img.png",
  genres: [5, 6],
  rate: 4.5,
  difficulty: 0,
  duration: {min: 15, max: 30},
  numberPeople: {min: 5, max: 10},
  followers: 27890
}, {
  id: 30,
  name: "Через пустыню",
  imgSrc: "./img.png",
  genres: [1],
  rate: 4.6,
  difficulty: 1,
  duration: {min: 30, max: 45},
  numberPeople: {min: 2, max: 5},
  followers: 14567
}, {
  id: 31,
  name: "Квадрополис",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.7,
  difficulty: 2,
  duration: {min: 60, max: 90},
  numberPeople: {min: 2, max: 4},
  followers: 18923
}, {
  id: 32,
  name: "Эксплодинг коты",
  imgSrc: "./img.png",
  genres: [7],
  rate: 4.4,
  difficulty: 0,
  duration: {min: 15, max: 30},
  numberPeople: {min: 2, max: 5},
  followers: 34567
}, {
  id: 33,
  name: "Механик",
  imgSrc: "./img.png",
  genres: [1, 4],
  rate: 4.8,
  difficulty: 2,
  duration: {min: 90, max: 120},
  numberPeople: {min: 2, max: 4},
  followers: 15678
}, {
  id: 34,
  name: "Скай Аллея",
  imgSrc: "./img.png",
  genres: [7],
  rate: 4.5,
  difficulty: 1,
  duration: {min: 45, max: 60},
  numberPeople: {min: 2, max: 4},
  followers: 20123
}];


export default games;
# Лабораторная №6 — Docker

## Архитектура сервисов

| Сервис    | Роль                         | Порт (снаружи) | Сеть           |
|-----------|------------------------------|----------------|----------------|
| `proxy`   | Reverse proxy (Nginx)        | `80`           | `boardmate_net`|
| `frontend`| React build + Nginx          | внутренний     | `boardmate_net`|
| `backend` | FastAPI                      | внутренний     | `boardmate_net`|
| `db`      | PostgreSQL 15                | внутренний     | `boardmate_net`|
| `minio`   | Объектное хранилище          | внутренний     | `boardmate_net`|

Схема запросов:

```text
Браузер → proxy:80
           ├─ /      → frontend:80 (статика React)
           └─ /api/* → backend:8000 (FastAPI)
```

Backend ходит в `db:5432` и `minio:9000` по внутренней сети Docker.

## Быстрый старт

```bash
cd FullStack
copy .env.example .env
docker compose up --build -d
```

Проверка:

- Приложение: http://localhost
- Health backend: http://localhost/health
- Swagger: http://localhost/docs

Остановка:

```bash
docker compose down
```

Полная очистка с томами:

```bash
docker compose down -v
```

## Файлы

- `docker-compose.yml` — оркестрация всех сервисов
- `nginx/proxy.conf` — reverse proxy
- `boardmate_back/Dockerfile` — backend
- `boardmate_back/.dockerignore`
- `boardmate_back/docker/entrypoint.sh` — ожидание БД и опциональный `INIT_DB`
- `boardmate_front/Dockerfile` — сборка React + Nginx
- `boardmate_front/nginx.conf` — SPA routing
- `.env.example` — шаблон переменных (без секретов в репозитории)

## Переменные окружения

Секреты и пароли задаются только в `.env` (файл в `.gitignore`).

Ключевые переменные:

- `SECRET_KEY` — JWT
- `POSTGRES_*`, `DB_*` — база данных
- `MINIO_*` — хранилище файлов
- `REACT_APP_API_URL` — URL API при сборке frontend (`/api` через proxy)
- `INIT_DB=true` — автоматическое создание таблиц при старте backend

## Healthcheck и порядок запуска

1. `db` — `pg_isready`
2. `minio` — старт контейнера
3. `backend` — после готовности `db`, endpoint `/health`
4. `frontend` — отдача статики
5. `proxy` — после готовности `backend` и `frontend`

## CI/CD

Workflow: `.github/workflows/ci.yml`

При push/pull request:

1. Тесты backend (`pytest`)
2. Тесты frontend (`npm test`)
3. Сборка Docker-образов (`docker compose build`)

## Локальная разработка без полного стека

Один `docker-compose.yml` в корне — можно поднять только нужные сервисы:

```bash
cd FullStack
docker compose up -d db minio
```

Backend и frontend при этом запускаются локально (`venv` + `npm start`), а БД и MinIO — в контейнерах.

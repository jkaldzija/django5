# Django DRF Skeleton

Production-ready Django REST Framework skeleton with:
- PostgreSQL
- JWT auth (`djangorestframework-simplejwt`)
- Celery + Redis (worker + beat)
- Docker Compose orchestration
- Custom user model (`email` as username)

## Run

```bash
docker-compose up --build
```

## Endpoints

- `GET /api/ping/`
- `POST /api/auth/register/` with JSON body:
  ```json
  {
    "email": "user@test.dev",
    "password": "test1234"
  }
  ```
- `POST /api/auth/login/` with JSON body:
  ```json
  {
    "email": "user@test.dev",
    "password": "test1234"
  }
  ```
- `POST /api/auth/refresh/` with JSON body:
  ```json
  {
    "refresh": "<refresh_token>"
  }
  ```
- `GET /api/users/me/` with `Authorization: Bearer <access_token>`

## Default test user

Created automatically on backend startup:
- Email: `user@test.dev`
- Password: `test1234`
# django5

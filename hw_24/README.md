# Book Library Application

A simple Django-based application with PostgreSQL database, Redis, Celery and Docker support.

## Features

- Add and manage your personal book collection
- Search for books by title, author, or genre
- Track your reading progress
- Connect with other book lovers
- Automated email notifications
- Background task processing with Celery
- Task monitoring with Flower

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Redis](https://redis.io/docs/latest/develop/get-started/)
- [PostgreSQL](https://www.postgresql.org/docs/15/tutorial-start.html)
- [Celery](https://docs.celeryq.dev/en/stable/getting-started/index.html)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/cross-development/ithillel-python-pro-course.git
cd ithillel-python-pro-course/hw_24
```

### 2. Create the `.env` file

Create a `.env` file in the project root with the following variables:

```
# Django settings
DEBUG=
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=

# Database
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=

# Celery
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=

# Email settings
EMAIL_BACKEND=
DEFAULT_FROM_EMAIL=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

### 3. Start the application

```bash
docker-compose up --build
```

### 4. Run migrations

In a separate terminal window, run:

```bash
docker-compose exec web python manage.py migrate
```

### 5. Create superuser (optional)

To create an admin user, run:

```bash
docker-compose exec web python manage.py createsuperuser
```

### 6. Access the application

- Web interface: [http://localhost:8000](http://localhost:8000)
- Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)
- API documentation: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Flower monitoring: [http://localhost:5555](http://localhost:5555)

## API Endpoints

- Register: `POST /api/register/`
- Login: `POST /api/login/`
- Refresh token: `POST /api/token/refresh/`
- Books list: `GET /api/books/`
- Book details: `GET /api/books/{id}/`
- Create book: `POST /api/books/`
- Update book: `PUT /api/books/{id}/`
- Delete book: `DELETE /api/books/{id}/`

## Celery Tasks

The application includes several Celery tasks:

1. **Registration Email**: Sends a welcome email immediately after user registration
2. **Promotional Email**: Sends a promotional email 10 minutes after user registration
3. **User Count Logger**: Logs the total number of users every 10 minutes

## Development

The project is set up with auto-reload capabilities, so any changes you make to Python files will automatically restart
the Django development server.

### Environment Variables

All configuration is handled through environment variables in the `.env` file:

- `DEBUG`: Enable debug mode (`True` or `False`)
- `SECRET_KEY`: Django secret key
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `POSTGRES_*`: Database configuration
- `CELERY_*`: Celery configuration
- `EMAIL_*`: Email configuration

### Data Persistence

- PostgreSQL data is stored in a Docker volume `postgres_data`
- Media files are stored in a Docker volume `media_data`

This ensures your data persists even when containers are removed.

## Docker Commands

- Start containers: `docker-compose up`
- Start containers in background: `docker-compose up -d`
- Stop containers: `docker-compose down`
- View logs: `docker-compose logs -f`
- Run Django management commands: `docker-compose exec web python manage.py [command]`
- Rebuild containers: `docker-compose up --build`

## Common Commands

### Database Management

- Apply migrations: `docker-compose exec web python manage.py migrate`
- Create migrations: `docker-compose exec web python manage.py makemigrations`
- Create superuser: `docker-compose exec web python manage.py createsuperuser`

### Static Files

- Collect static files: `docker-compose exec web python manage.py collectstatic`

### Celery

- View Celery worker logs: `docker-compose logs -f celery`
- View Celery beat logs: `docker-compose logs -f celery_beat`
- Monitor tasks with Flower: http://localhost:5555
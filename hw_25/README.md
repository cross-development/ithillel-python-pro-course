# Chat Application

A real-time Django Channels-based chat application with PostgreSQL database, Redis, WebSocket support, and Docker integration.

## Features

- Real-time messaging between users
- Public and private chat rooms
- WebSocket communication using Django Channels
- Asynchronous message handling
- User authentication
- Admin panel for managing chats and users
- Dockerized environment with PostgreSQL and Redis

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Redis](https://redis.io/docs/latest/develop/get-started/)
- [PostgreSQL](https://www.postgresql.org/docs/15/tutorial-start.html)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/cross-development/ithillel-python-pro-course.git
cd ithillel-python-pro-course/hw_25
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
POSTGRES_HOST=
POSTGRES_PORT=

# WebSockets
CHAT_BROKER_URL=
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

## WebSocket Endpoints

- Connect to WebSocket: `ws://localhost:8000/ws/chat/<room_name>/`

## Development

The project is configured for hot-reloading during development. Any changes to Python files will automatically restart the Django server.

### Environment Variables

- `DEBUG`: Enable debug mode (`True` or `False`)
- `SECRET_KEY`: Django secret key
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `POSTGRES_*`: Database configuration
- `CHAT_*`: Redis configuration for Django Channels

### Data Persistence

- PostgreSQL data is stored in the `postgres_data` Docker volume.

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

## Notes

- WebSocket communication uses Django Channels with Redis as the backing layer.
- Ensure Redis is running properly when using WebSockets.
- PostgreSQL database persists between container rebuilds through Docker volumes.


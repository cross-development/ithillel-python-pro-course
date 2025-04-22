# "Hello, world!" Application

A simple Django-based application with PostgreSQL database and Docker support.

## Features

- Create, read, update, and delete tasks
- Mark tasks as completed/incomplete
- Attach images to tasks
- Set due dates for tasks
- Responsive design with Bootstrap
- Environment variables configuration support

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/cross-development/ithillel-python-pro-course.git
cd ithillel-python-pro-course
```

### 2. Create the `.env` file

Create a `.env` file in the project root with the following variables:

```
# Django settings
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=

# Database settings
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
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

## Development

The project is set up with auto-reload capabilities, so any changes you make to Python files will automatically restart the Django development server.

### Environment Variables

All configuration is handled through environment variables in the `.env` file:

- `DEBUG`: Enable debug mode (`True` or `False`)
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `POSTGRES_*`: Database configuration

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

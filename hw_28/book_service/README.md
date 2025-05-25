# Book Library Application

A Django-based microservices application integrating:

* **Book Library** features with PostgreSQL, Redis, Celery and Docker support
* **Real-time WebSocket** chat powered by Django Channels and Redis
* **RabbitMQ** notifications consumer for customer events

## Features

* **Book Library**

    * Add and manage your personal book collection
    * Search by title, author, or genre
    * Track reading progress
    * User registration and authentication via REST API

* **Chat Application**

    * Real-time messaging in public and private rooms
    * WebSocket communication using Django Channels
    * Asynchronous message broadcasting via Redis
    * Admin panel for user and chat management

* **Notification Service**

    * Background RabbitMQ consumer for `customer.created` and `customer.updated`
    * Sends email notifications (configurable via Django email backend)
    * Management command to launch consumer

* **Background Tasks**

    * Celery for task scheduling and execution
    * Flower monitoring UI

## Prerequisites

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Redis](https://redis.io/docs/latest)
* [PostgreSQL](https://www.postgresql.org/docs/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Celery](https://docs.celeryq.dev/en/stable/)

## Getting Started

### 1. Clone the repository

```bash
    git clone https://github.com/cross-development/ithillel-python-pro-course.git
    cd ithillel-python-pro-course/hw_28
```

### 2. Create the `.env` file

At the project root, create a `.env` containing:

```
# Django settings
# Django settings
DEBUG =
SECRET_KEY =
DJANGO_ALLOWED_HOSTS =
DJANGO_SETTINGS_MODULE =

# Database
POSTGRES_DB =
POSTGRES_USER =
POSTGRES_PASSWORD =
DB_HOST =
DB_PORT =

# Celery
CELERY_BROKER_URL =
CELERY_RESULT_BACKEND =

# Email settings
EMAIL_BACKEND =
DEFAULT_FROM_EMAIL =
EMAIL_HOST =
EMAIL_PORT =
EMAIL_USE_TLS =
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD =

# WebSockets
CHAT_BROKER_URL =

# RabbitMQ settings
RABBITMQ_HOST =
RABBITMQ_USER =
RABBITMQ_PASS =
```

### 3. Build and run services

```bash
docker-compose up --build
```

This brings up:

* **web**: Django app on [http://localhost:8000](http://localhost:8000)
* **postgres**: PostgreSQL database
* **redis**: Redis for Channels and Celery
* **rabbitmq**: RabbitMQ broker
* **celery**: Celery worker and beat
* **flower**: Celery monitoring on [http://localhost:5555](http://localhost:5555)

### 4. Apply migrations

```bash
docker-compose exec web python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
docker-compose exec web python manage.py createsuperuser
```

### 6. Collect static files

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

## Access URLs

* **Web UI**: [http://localhost:8000](http://localhost:8000)
* **Admin**: [http://localhost:8000/admin](http://localhost:8000/admin)
* **API docs**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
* **WebSocket**: `ws://localhost:8000/ws/chat/<room_name>/`
* **Flower**: [http://localhost:5555](http://localhost:5555)

## Celery Tasks

* **Registration Email**: Sends welcome email on user registration
* **Promotional Email**: Sends promo email 10 minutes after registration
* **User Count Logger**: Logs total user count every 10 minutes

## RabbitMQ Notifications

* **Exchange**: `customer_events` (topic)
* **Routing Keys**: `customer.created`, `customer.updated`
* Consumer is launched via `python manage.py runconsumer`

## Docker Commands

* **Start**: `docker-compose up`
* **Start detached**: `docker-compose up -d`
* **Stop**: `docker-compose down`
* **Logs**: `docker-compose logs -f`
* **Rebuild**: `docker-compose up --build`
* **Run management**: `docker-compose exec web python manage.py <command>`

## Notes

* Ensure Redis and RabbitMQ services are healthy before running the web app.
* Django Channels uses Redis for WebSocket layer; Celery uses Redis broker.
* RabbitMQ consumer depends on RabbitMQ and prints email simulation to console or sends via real SMTP based on
  configuration.

# Notification Service

A Python microservice that listens to RabbitMQ events and sends emails when a user is created or updated.

## Features

* Listens to `user.created` and `user.updated` events from RabbitMQ
* Sends an email with user details using SMTP
* Graceful reconnection logic
* Dockerized for isolated operation

## Prerequisites

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)
* RabbitMQ (provided via Docker Compose)

## Getting Started

1. **Clone the repo**

   ```bash
    git clone https://github.com/cross-development/ithillel-python-pro-course.git
    cd ithillel-python-pro-course/hw_25
   ```

2. **Build & start just this service**

   ```bash
   docker-compose up --build notification_service
   ```

3. **Simulate a message manually (optional)**

   ```bash
   docker-compose exec rabbitmq bash
   rabbitmqadmin publish exchange=user_events routing_key=user.created payload='{"email": "test@example.com", "first_name": "Test", "last_name": "User"}'
   ```

4. **Create the `.env` file**

Create a `.env` file in the project root with the following variables:

```
# Django settings
DEBUG=
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=

# Email settings
EMAIL_BACKEND=
DEFAULT_FROM_EMAIL=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

# RabbitMQ settings
RABBITMQ_HOST=
RABBITMQ_USER=
RABBITMQ_PASS=
```

## Docker Commands

* **Build & run**
  `docker-compose up --build notification_service`
* **Logs**
  `docker-compose logs -f notification_service`
* **Stop all**
  `docker-compose down`

## Notes

Message queue uses RabbitMQ with topic exchange `user_events`.
SMTP configuration depends on your email provider (e.g., Gmail, Mailgun, etc).

# Customer Service

A Django REST microservice responsible for customer CRUD operations and publishing customer events to RabbitMQ.

## Features

* CRUD API for Customer model (email, first name, last name)
* Publishes `customer.created` and `customer.updated` events to RabbitMQ
* SQLite database for simplicity
* Dockerized with Docker Compose

## Prerequisites

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)
* RabbitMQ (provided via Docker Compose)

## Getting Started

1. **Clone the repo**

   ```bash
    git clone https://github.com/cross-development/ithillel-python-pro-course.git
    cd ithillel-python-pro-course/hw_27
   ```

2. **Build & start just this service**

   ```bash
   docker-compose up --build customer_service
   ```

3. **Run migrations**

   ```bash
   docker-compose exec customer_service python manage.py migrate
   ```

4. **Use the API**

    * Create a customer:

      ```bash
      curl -X POST http://localhost:8000/customers/ \
        -H "Content-Type: application/json" \
        -d '{"email":"test@example.com","first_name":"John","last_name":"Doe"}'
      ```
    * Update a customer:

      ```bash
      curl -X PATCH http://localhost:8000/customers/1/ \
        -H "Content-Type: application/json" \
        -d '{"first_name":"Jane"}'
      ```

Every create/update emits a message to the `customer_events` exchange in RabbitMQ.

5. **Create the `.env` file**

Create a `.env` file in the project root with the following variables:

```
# Django settings
DEBUG=
SECRET_KEY=
DJANGO_ALLOWED_HOSTS=

# RabbitMQ settings
RABBITMQ_HOST=
RABBITMQ_USER=
RABBITMQ_PASS=
```

## Docker Commands

* **Build & run**
  `docker-compose up --build customer_service`
* **Run management commands**
  `docker-compose exec customer_service python manage.py <command>`
* **Stop all**
  `docker-compose down`

## Notes

Uses Django signals to publish events on `post_save`.
Exchange: `customer_events` (type: topic).
Routing keys: `customer.created`, `customer.updated`.

# fast-api-base

Basic python project that allows for a simple API to be stood up quickly.

## Testing

Run `make test` at console.
Checks for flake8 compatibility first and then runs pytest.

## Running Locally

Run `docker-compose build` then `docker-compose up`.
It is setup to allow for hot-swap reloads for ease of development.

## Swagger docs

Run the container locally and go to `localhost:8080/docs`

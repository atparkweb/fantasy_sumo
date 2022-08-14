# Fantasy Sumo Application

This is a Django based web application for creating and participating in
Fantasy Sumo tournaments.


## Development
The development environment (Python/Django, Postgres) is configured to use [Docker](https://www.docker.com) containers.

### Requirements
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running the server
Use the following steps to get the Django development server running with Postgres:
1. In a terminal `cd` to the root of this project
2. Run `docker compose -f ./docker/dev/docker-compose.yml --project-directory . up`
3. Open browser and go to [localhost:8000](http://localhost:8000)
4. Start hacking

### Running Django commands
Since the Python/Django environment is in containers, all django commands run through docker

#### Django Scripts
1. In a terminal `cd` to the root of this project
2. Run `docker compose -f ./docker/dev/docker-compose.yml --project-directory . run web python manage.py <COMMAND>`

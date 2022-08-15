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
2. Run `./scripts/composeup`
3. Open browser and go to [localhost:8000](http://localhost:8000)
4. Start hacking

### Stopping the server
1. In a terminal `cd` to the root of this project
2. Run `./scripts/composedown`

### Running Migrations
1. In a terminal `cd` to the root of this project
2. Run `./scripts/migrate`

### Connecting to DB container psql
1. Run `docker exec -it <DB container name> psql -U postgres -W postgres`


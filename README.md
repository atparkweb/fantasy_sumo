# Fantasy Sumo Application

This is a Django based web application for creating and participating in
Fantasy Sumo tournaments.


## Development
The development environment (Python/Django, Postgres) is configured to use [Docker](https://www.docker.com) containers.

### Requirements
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Configuring Environment
To run the containers, first create a `.env` file in the root directory.
Use the `.env.example` file to see the required variables.

One of the environment variables should be `SECRET_KEY` to generate a Django key:
Run `./scripts/genkey`

and copy and paste the value into the `.env` file without quotes:
`SECRET_KEY=example_hjad7*&^fj4lksfd_(`

### Running the server
Use the following steps to get the Django development server running with Postgres:
1. In a terminal `cd` to the root of this project
2. Run `./scripts/composeup`
3. Open browser and go to [localhost:8000](http://localhost:8000)
4. Start hacking

### Django Admin
The backend admin can be accessed through the [Admin Interface](http://localhost:8000/admin)
Refer to the Official Django documentation on setting up admin access.

### Stopping the server
In a terminal from the the project root run: `./scripts/composedown`

### Generating Migrations
In a terminal from the project root run: `./scripts/makemigrations`

### Running Migrations
In a terminal from the project root run: `./scripts/migrate`

### Connecting to DB container psql
If you want to connect to the database through PSQL:
1. Run `docker exec -it <DB container name> psql -U postgres`


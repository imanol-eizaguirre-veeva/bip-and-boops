# Job Skills Call

Clone the repository, follow the installation instructions below and start the 
application as documented. 

Look around, familiarize yourself with the code structure and feel free to ask 
questions at any time.

# Prerequesites

This project can be run easily with [Docker](https://www.docker.com/). Alternatively, 
you can also run it  directly on your operative system, and for that, you would 
need the following:

Backend:

* Python 3.12
* pipx

Frontend:

* Node >= v18

Disclaimer: A preconfigured `.env` file is provided as part of the repository,
although normally this file would be excluded from it.


# Running the project with Docker

If you have Docker installed in your machine, you simply need to build the 
containers by executing the following command from the root of the project:

```bash
docker-compose build
```

which should give you the following output if everything worked out (the time
will vary depending on your machine's specifications):

```
[+] Building 17.0s (32/32) FINISHED
```

Afterward, you can run the containers by executing:

```bash
docker-compose up
```

You should see logs from the 3 services: `backend`, `mongo`, `frontend`.

## Run the Backend tests

You can run the tests by simply running:

```bash
docker exec -it backend pytest
```

# Running the project in your machine

## Backend

You will need to run this project in a virtual environment to ensure that the 
libraries required for this code to work are isolated from the ones in your system.

In case you don't have [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
already installed, please run the following (`pipxp` will ensure that `virtualenv` 
is installed into an isolated environment):

```bash
pipx install virtualenv
```

#### Create a virtual environment and install the requirements
Create the environment (creates a folder in your current directory)

```bash
virtualenv env_name
```

In Linux or Mac, activate the new python environment:

```bash
source env_name/bin/activate
```

If you are on Windows:

```bash
.\env_name\Scripts\activate
```

Confirm that the env is successfully selected by running:

```bash
which python3
```

Now you are ready to install the requirements:

```bash
pip install -r requirements.txt
```

### Run the project

The code is in the `api` folder:

1. Access the backend folder (`cd backend`)
2. Run the server: `fastapi run app/main.py`
3. In a browser, open: `http://0.0.0.0:8000`


### Run the Backend tests

You can run the tests by simply running:

```bash
pytest
```

## MongoDB

We made an in-memory MongoDB available in case you run it manually. You can
launch it by following these steps:

1. Navigate to the `util/db` folder
2. Install dependencies: `npm ci`
3. Start: `npm run testdb`

## Frontend

The code is in the `ui` folder:

1. Navigate to the `ui` folder
2. Install dependencies: `npm ci`
3. Start: `npm run start`
4. In a browser, open `http://0.0.0.0:4200`


# OpenAPI Documentation

This project contains OpenAPI automatic UI documentation:

* Swagger UI is found on `/docs`
* ReDoc UI is found on  `/redoc`

# Usage

## Authentication

You can authenticate in the following endpoint: `/api/v1/auth/token` using
the following parameters:

* username: `1234567890`
* password: `secret`

Which will generate the following token (valid for 1 hour):

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.1OURXfxWcaT1DOs-abEis6N3RhQfIVWsUjv1VaUyev0`

By default, the UI server listen on port `4200` and the API listen on the port `8000`.

The API endpoints are protected with a JWT, to test queries manually, you can 
use the token mentioned above and inject it in the `Authorization` header 
prefixed with `Bearer `.

To simulate another user, you can encode a new payload (e.g. by using 
`https://jwt.io/` tool), for that, you need to use the algorithm `HS256` and 
the secret `veeva`. Here is an example of the payload before encoding (sub is 
the user identifier):

```json
{
  "sub": "1234567890"
}
```

Request example using cURL:

```bash
curl --request GET \
  --url http://localhost:8000/api/v1/page \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.1OURXfxWcaT1DOs-abEis6N3RhQfIVWsUjv1VaUyev0'
```

## API Endpoints

* `GET /api/v1/page`: returns the list of pages defined in the database (this is used in the UI to simplify access to the page statistics)
* `GET /api/v1/stats/page/:pageID/active`: returns the number of unique users having been active on a page identified by `:pageID` (an UUIDv4 identifier) in a given time period (defined with an environment variable in `apps/api/.env`).
* `GET /api/v1/view?countries[]=Germany&countries[]=...&browsers[]=Germany&browsers[]=...`: returns the list of views defined in the database with the possibility to provide optional filters for origin country and client browser
* `GET /api/v1/view/page/:pageID`: returns all the views for a single page.
* `POST /api/v1/view`: Registers a view in the database.

Example Payload:

```json
{
  "pageID": "38f92553-00a3-43d1-91fb-9329ce2f3673", // UUIDv4
  "country": "Germany", // ISO 3166
  "browser": "Firefox" // can be alphanumeric, useful if version have to be specified
}
```
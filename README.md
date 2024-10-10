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

Additionally you can run the tests by simply running:

```bash
docker exec -it backend pytest
```

# Usage

## OpenAPI Documentation

This project contains OpenAPI automatic UI documentation:

* Swagger UI is found on `/docs`
* ReDoc UI is found on  `/redoc`

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

# Exercise

When checking the views per page (test data is in the DB when you start it), we 
have a stat “Active users in the last 30mins”. 

We’d like to have a second stat that gives the number of “Recurring users in 
the last hour for a given page”, i.e. such users from the DB that visited the 
same page twice or more within the last hour.

## Acceptance Criteria

* Extend the backend API to have another endpoint for the statistic described in 
the task above. The endpoint should take the request parameters and return the 
computed statistic “Recurring users in the last hour for a given page”.
* Extend the frontend dashboard page to call the API and show the statistic in a 
second graph component.
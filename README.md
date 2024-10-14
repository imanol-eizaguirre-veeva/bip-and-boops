# Bip and Boops

This exercise tries to replicate a regular-day-task at work.

Clone the repository, follow the instructions below, and once you have understood 
the task, start the application as documented.

Look around, familiarize yourself with the code structure and feel free to ask 
questions at any time. The interviewers in the call are there to support you.

## Project Description

This is a fullstack project that replicates the behaviour of Googe Analytics:

* Each document in the database represents a page view.
* A simple frontend UI displays the list of different pages and their stats.
* An API to retrieve the data, and to add new records.

Visiting the stats of a page in the frontend UI won't add a page view in the
database, in the same way Google Analytics does not register page views for the 
pages when you check their stats within Google Analytics. 
This can only be done by using the API.

## Data Schema

Example of a database document:

```json
{
  "pageID": "38f92553-00a3-43d1-91fb-9329ce2f3673",
  "UTCDateTime": "2024-09-25T13:21:43.951+00:00",
  "country": "Germany",
  "browser": "Firefox" ,
  "userID" : "2",
}
```

## API Endpoints

The project has the following endpoints:

`GET /api/v1/page`
* returns the list of unique page IDs (used in the UI to simplify access to the page statistics)

`GET /api/v1/stats/page/:pageID/active`
* returns the number of unique users that visited a page (identified by `:pageID`, a UUIDv4) in the last 30 minutes (you'll get this data when accessing the page details in the UI).

`GET /api/v1/view?countries[]=Germany&countries[]=...&browsers[]=Germany&browsers[]=...`
* returns the list of page views, with the option to filter by country and browser

`GET /api/v1/view/page/:pageID`
* returns all the page views for a single page.

`POST /api/v1/view`
* Registers a new view for a page.

This project contains OpenAPI automatic UI documentation that cab found on 
http://localhost:8000/docs.

This offers a friendlier and easier to use interface that the command line,
although you are free to use whatever you prefer.

# Exercise

In our API we have a stat called “Active users in the last 30 mins”, and we'd 
like to have an additional stat.

This new one should retrieve the number of “Recurring users in 
the last hour for a given page”. This means: the number of users that visited
a page at least twice during the last hour.

## Acceptance Criteria

* Extend the backend API to have another endpoint for the statistic described 
above. The endpoint should take the request parameters and return the 
computed statistic “Recurring users in the last hour for a given page”.

# Run the project

You need to build the containers by executing the following command from the root of the project:

```bash
docker-compose build
```

Afterward, you can run the containers by executing:

```bash
docker-compose up
```

You should see logs from the 3 services: `backend`, `mongo`, `frontend`.
Verify that all 3 of them are running without issues.

The UI server listens on port `4200` and the API listens on the port `8000`.

## Authentication

You can authenticate in the following endpoint: `/api/v1/auth/token` using
the following parameters:

* username: `1234567890`
* password: `secret`

Which will generate the following token (valid for 1 hour):

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.1OURXfxWcaT1DOs-abEis6N3RhQfIVWsUjv1VaUyev0`

Request example using cURL:

```bash
curl --request GET \
  --url http://localhost:8000/api/v1/page \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.1OURXfxWcaT1DOs-abEis6N3RhQfIVWsUjv1VaUyev0'
```




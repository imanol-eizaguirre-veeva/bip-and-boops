# Bip and Boops

This is an API that replicates the behaviour of Googe Analytics:

* we store page view events in our database 
* we provide insights about the page view events (e.g. total number of views, number of active users, etc)

# Exercise

In the API there's an endpoint that returns the “Active users in the last 30 mins”, 
and we'd like to have an additional endpoint to get the “Recurring users in 
the last hour for a given page”, which would return the number of users that 
visited a page at least twice during the last hour. 

# How to run the project

You need to build the containers by executing the following command from the root of the project:

```bash
docker-compose build
docker-compose up
```

You should see logs from the 3 services: `backend`, `mongo`.
Verify that everything is running by accessing `http://localhost:8000/docs`,
authenticating, and querying the data.

## Authentication

You can authenticate using the following parameters:

* username: `1234567890`
* password: `secret`

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
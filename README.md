# Bip and Boops

This is an API that replicates the behaviour of Google Analytics:

* we store page view events in our database in the `pageviews` collection
* we provide insights about the page view events (e.g. total number of views, number of active users, etc)

# Exercise

There's an endpoint that returns the `Active users in the last 30 mins` and we'd like to have
an additional endpoint to get the `Recurring users in the last hour for a given page`, which
should return the number of users that visited a page at least twice during the last hour.

* Active user: there's at least one document in the database for a `userID` in the last 30 minutes.
* Recurring user: there's more than one document with the same `userID` for a given `pageID` in the last hour.

# How to run the project

You need to build the containers by executing the following commands from the root of the project:

```bash
docker-compose build
docker-compose up
```

You should see logs from the 2 services: `backend`, `mongo`.

Verify that everything is running by accessing the Swagger UI at `http://localhost:8000/docs` and querying the data.

## Data Schema

Here is an example of a database document in the `pageviews` collection:

```json
{
  "pageID": "38f92553-00a3-43d1-91fb-9329ce2f3673",
  "UTCDateTime": "2024-09-25T13:21:43.951+00:00",
  "country": "Germany",
  "browser": "Firefox" ,
  "userID" : "2",
}
```

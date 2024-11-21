db = db.getSiblingDB('analytics'); 
const now = Date.now();

db.pageviews.insertMany([
  {
      "pageID" : "38f92553-00a3-43d1-91fb-9329ce2f3673",
      "UTCDateTime" : new Date(now - 10 * 60 * 1000),
      "country" : "France",
      "browser" : "Chrome",
      "userID" : "2",
  },
  {
    "pageID" : "38f92553-00a3-43d1-91fb-9329ce2f3673",
    "UTCDateTime" : new Date(now - 5 * 60 * 1000),
    "country" : "Germany",
    "browser" : "Firefox",
    "userID" : "1",
  },
  {
    "pageID" : "49acf0e6-6a37-491f-9102-6cbe47e5bf01",
    "UTCDateTime" : new Date(now - 32 * 60 * 1000),
    "country" : "Italy",
    "browser" : "Chrome",
    "userID" : "3",
  },
  {
    "pageID" : "49acf0e6-6a37-491f-9102-6cbe47e5bf01",
    "UTCDateTime" : new Date(now - 27 * 60 * 1000),
    "country" : "Italy",
    "browser" : "Chrome",
    "userID" : "3",
  },
  {
    "pageID" : "49acf0e6-6a37-491f-9102-6cbe47e5bf01",
    "UTCDateTime" : new Date(now - 40 * 60 * 1000),
    "country" : "Germany",
    "browser" : "Safari",
    "userID" : "1",
  },
  {
    "pageID" : "49acf0e6-6a37-491f-9102-6cbe47e5bf01",
    "UTCDateTime" : new Date(now - 70 * 60 * 1000),
    "country" : "Germany",
    "browser" : "Safari",
    "userID" : "1",
  },
  {
    "pageID" : "38f92553-00a3-43d1-91fb-9329ce2f3673",
    "UTCDateTime" : new Date(now - 25 * 60 * 1000),
    "country" : "France",
    "browser" : "Chrome",
    "userID" : "2",
  },
  {
    "pageID" : "49acf0e6-6a37-491f-9102-6cbe47e5bf01",
    "UTCDateTime" : new Date(now - 25 * 60 * 1000),
    "country" : "Italy",
    "browser" : "Chrome",
    "userID" : "3",
  },
]);

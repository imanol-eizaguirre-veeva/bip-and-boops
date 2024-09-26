const prompt = require('prompt-sync')();
const MongoMemoryServer =
  require('mongodb-memory-server-global').MongoMemoryServer;
const MongoClient = require('mongodb').MongoClient;
const DATA = require('./data');

async function doIt() {
  const mongod = new MongoMemoryServer({
    instance: { port: 57202 },
  });

  await mongod.start(true);

  const uri = await mongod.getUri('analytics');

  // insert test data
  const conn = await MongoClient.connect(uri);
  await conn.db().collection('pageviews').insertMany(DATA);

  console.log();

  prompt('Database running on ' + uri + ' (enter key to end)');

  await mongod.stop();
}

doIt()
  .then(() => console.log('ended'))
  .catch(console.log);

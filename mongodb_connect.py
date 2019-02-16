import pymongo
client = pymongo.MongoClient("mongodb://peranki:#cd3amsAXUW5UJ79@firecry-shard-00-00-oxlvg.gcp.mongodb.net:27017,firecry-shard-00-01-oxlvg.gcp.mongodb.net:27017,firecry-shard-00-02-oxlvg.gcp.mongodb.net:27017/test?ssl=true&replicaSet=FireCry-shard-0&authSource=admin")
db = client.test

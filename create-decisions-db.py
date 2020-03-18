files = ['CIV', 'COM', 'CRIM', 'SOC']
civ = open('test_set/CIV').read().split("<<<<<<<<<<NEW>>>>>>>>>>")
com = open('test_set/COM').read().split("<<<<<<<<<<NEW>>>>>>>>>>")
crim = open('test_set/CRIM').read().split("<<<<<<<<<<NEW>>>>>>>>>>")
soc = open('test_set/SOC').read().split("<<<<<<<<<<NEW>>>>>>>>>>")

import utils.mongo as um

config = {
	"host" : "localhost",
	"port" : "27017",
	"username" : "",
	"password" : ""
}

db = _connect_mongo('decisions', config['host'], config['port'], config['username'], config['password'])
db.decisions.insert_many([{'class' : 'com', 'text' : doc} for doc in com])
db.decisions.insert_many([{'class' : 'civ', 'text' : doc} for doc in civ])
db.decisions.insert_many([{'class' : 'crim', 'text' : doc} for doc in crim])
db.decisions.insert_many([{'class' : 'soc', 'text' : doc} for doc in soc])

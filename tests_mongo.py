from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
db= client ['teststore']
collection =db['products']

##collection.insert_one({"_id":1,"Name":"keyboard","Price":300})
#collection.insert_many([{"_id":6,"Name":"Monitor","Price":520},
#	{"_id":7,"Name":"Super HDMI cable","Price":470},
#	{"_id":8,"Name":"Headphones pro","Price":570},
#	{"_id":9,"Name":"MousePad pro","Price":990}])







#results= collection.find({}).sort([("Price",1)])

#results= collection.find({"Price": {'$gt': 500 }})
#results = collection.find ({"Name": {'$regex':'.*pro.*','$options':'i'}})

#collection.insert_one({"_id":10,"Name":"Desk","Price":800,"Type": "Furniture"})

#collection.ensure_index([
 #   ('Type', 1),
  #  ('Price', 1),
   # ('Name', 1)])

results = collection.find ()



for r in results:
	print (r)




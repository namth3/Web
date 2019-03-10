from pymongo import MongoClient
url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1.connect
client = MongoClient(url)


#2. Get DB
db = client.c4e

#3. get collection
posts = db["posts"]
customers = db["customers"]
rivers = db["river"]


# #4. create new document
# new_post = {
#     "name" :"So huyet",
#     "price": 30000
# } #document


# #5. Insert new documnet into collection

# food_collection.insert_one(new_food)


#5. close connection
def close():
    client.close()
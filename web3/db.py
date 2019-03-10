from pymongo import MongoClient
url = "mongodb+srv://namth3:MN1Cbt6BFOvUIExD@cluster0-kondi.mongodb.net/test?retryWrites=true"

#1.connect
client = MongoClient(url)


#2. Get DB
db = client.test

#3. get collection
food_collection = db["food"]


#4. create new document
new_food = {
    "name" :"So huyet",
    "price": 30000
} #document


#5. Insert new documnet into collection

food_collection.insert_one(new_food)


#6. close connection
def close():
    client.close()
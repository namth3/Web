from db import food_collection
from pprint import pprint
from bson import ObjectId

def add_food(name:str,price:int):
    new_food = {"name":name,"price":price}
    food_collection.insert_one(new_food)

def get(query): # filter, limit = 5, skip = 10
    food_list = food_collection.find(query)
    return food_list

def get_by_id(id):
    food_list = food_collection.find_one({"_id": ObjectId(id)})
    return food_list

def delete_by_id(id):
    food_collection.delete_one(c)
    pass

def update_by_id(id,name, price):
    query = {"_id": ObjectId(id)}
    updater = {"$set": { "price": price, "name": name} }# $inc, $dec, $set, $unset
    food_collection.find_one_and_update(query,updater)

if __name__ == "__main__":
    update_by_id("5c81284e13be9715bcba0d75", "Tay gau", 5000000)
    # query = {"_id": ObjectId("5c81284e13be9715bcba0d75")}
    # updater = {"$set": { "price": 10000} }# $inc, $dec, $set, $unset
    # food_collection.find_one_and_update(query,updater)
    print(*get({}), sep = "\n")

    # delete_by_id("5c81245c13be970d38e1c6ab")
    # f = get_by_id("5c81245c13be970d38e1c6ab")
    # if f != None:
    #     print(f["name"])
    # else:
    #     print("Not found")


#     for food in get({
#             "_id": ObjectId("5c81245c13be970d38e1c6ab")
# }):
#         print(food["name"])
#         print(food["price"])
    # cursor = food_collection.find({})
    # cursor[0]["name"]
    # cursor[0]["price"]
    # for document in cursor:
    #     print(document["name"])
    #     print(document["price"])
# loop= True
# while loop == True:
#     request = input("Do you want to add more food to collection(Y/N)? ")
#     if request != "Y":
#         loop = False
#         pass
#     else:
#         name = input("What your favorite food? ")
#         price_str = input("What does this cost? ")
#         price = int(price_str)
#         add_food(name,price)
#     print_food()


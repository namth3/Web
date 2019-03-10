from db import food_collection
from pprint import pprint

def add_food(name:str,price:int):
    new_food = {"name":name,"price":price}
    food_collection.insert_one(new_food)

def print_food():
    cursor = food_collection.find({})
    for document in cursor: 
        pprint(document["name"])
        pprint(document["price"])
if __name__ == "__main__":
    food_list = food_collection.find(
        {
            "price": {"$gt": 25000}
        }
    )
    for food in food_list:
        print(food["name"])
        print(food["price"])
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


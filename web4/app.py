from db import food_collection
from flask import Flask, render_template, request
import food
app = Flask(__name__)

# 1. Create food_list 

@app.route("/food_list")

def menu():
    items = food.get({})
    return render_template("food_list.html", menu = items, user = "Ta Hai Nam")

# 2. Creat food_list detail

@app.route("/food_list/<id>")

def food_detail(id):
    dish = food.get_by_id(id)
    return render_template("food_detail.html", item = dish)

# 3. Create form to add new food

@app.route("/add_food", methods = ['GET','POST'])

def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        n = form["name"]
        p = form["price"]
        food.add_food(n,p) 
    return 'New food has been added to list:\n' + ' Food:\n'+ n +'Price:\n' +p


if __name__ == '__main__':
  app.run(debug=True)
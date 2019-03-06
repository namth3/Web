from flask import Flask, render_template, request
app = Flask(__name__)

items = [
  {"model":"FORD", 
  "daily_fee":2500000, 
  "image":"https://otothanhxuanford.com/wp-content/uploads/d3.jpg", 
  "time": 2019},
]

# @app.route("/")
# def menu():  
#     return render_template("menu.html",menu = items, user = "H.Duc")

# @app.route("/food/<int:i>")
# def food(i):
#     return render_template("food_detail.html", item = items[i])

@app.route("/new_bike", methods = ['GET','POST'])
def add_food():
    if request.method == "GET":
        return render_template("bike_form.html")
    elif request.method == "POST":
        form = request.form
        print(form)
        m = form["model"]
        d = form["daily_fee"]
        i = form["image"]
        y = form["time"]
        new_item= {"model":m, 
          "daily_fee":d, 
          "image":i, 
          "year":y}
        items.append(new_item)
        return str(items)


if __name__ == '__main__':
  app.run(debug=True)
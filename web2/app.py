from flask import Flask, render_template, request
app = Flask(__name__)

items = [
    {"name": "Com rang","price": 25000
    },
    {"name": "Pho bo","price": 30000},
    {"name": "Xoi xeo", "price": 10000},
]

# @app.route("/")
# def menu():  
#     return render_template("menu.html",menu = items, user = "H.Duc")

# @app.route("/food/<int:i>")
# def food(i):
#     return render_template("food_detail.html", item = items[i])

@app.route("/add_food", methods = ['GET','POST'])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        print(form)
        n = form["name"]
        p = form["price"]
        new_item= {"name":n, "price":p}
        items.append(new_item)
        return n + ":" + str(p)


if __name__ == '__main__':
  app.run(debug=True)
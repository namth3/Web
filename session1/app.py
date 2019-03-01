# from flask import Flask


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello C4E, this is our homepage"

# if __name__== "__main__":
#     print("run")
#     app.run(debug = True, port = 6969)
# #local host: 127.0.0.1
from flask import Flask
app = Flask(__name__)
#binding route with view function
@app.route("/") #router
def home(): # view function
    return "Hello C4E, this is our homepage"

@app.route("/myclass")
def myclass():
    return "C4E26"
@app.route("/hi/<name>")
def hiduc(name):
    return "Hi, {}".format(name)
@app.route("/add/<a>/<b>")
def add(a,b):
    a = int(a)
    b = int(b)
    c = str(a+b)
    return c
menu_lst = ["com","pho","chao"]
@app.route("/menu")
def menu():
    return str(menu_lst)
@app.route("/menu/<index>")
def menu_0(index):
    inx = int(index)
    food = menu_lst[inx]
    return food
    

if __name__ == '__main__':
  app.run(debug=True)
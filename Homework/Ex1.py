#Create new Flask app
from flask import Flask, redirect
app = Flask(__name__)


#Create route /about-me
@app.route("/about-me")
def info():
    info = {"Name": "Nam","Job": "Officer","School" :"FTU","Hobbies" :"Travel"}
    return str(info)

#Create route /school
@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)




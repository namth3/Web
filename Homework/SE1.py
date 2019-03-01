#Create new Flask app
from flask import Flask, redirect
app = Flask(__name__)


#Create BMI
@app.route("/bmi/<w>/<h>")
def BMI(w,h):
    BMI_calc = 10000*int(w)/(int(h)**2)
    if BMI_calc < 16:
      mess = "BMI = {:.2f} < 16 : Severely underweight".format(BMI_calc)
    elif BMI_calc < 18.5:
      mess = "16 <= BMI = {:.2f} < 18 : Underweight".format(BMI_calc)
    elif BMI_calc < 25:
      mess = "18 <= BMI = {:.2f} < 25 : Normal".format(BMI_calc)
    elif BMI_calc < 30:
      mess = "25 <= BMI = {:.2f} < 30 : Overweight".format(BMI_calc)
    else:
      mess = "BMI = {:.2f} > 30 : Normal".format(BMI_calc)
    return mess

#Creat route /user/<name>
@app.route("/user/<name>")
def username(name):
  Users = { "huy":{"name":"Nguyen Quang Huy", 
                          "location":"Hanoi", 
                          "Job":"Teacher"},
                "duc":{"name":"Hoang Huy Duc",
                          "location":"HaiPhong",
                          "Job":"T.A"},
                "nam":{"name":"Ta Hai Nam",
                          "location":"PhuTho",
                          "Job":"Student"}
                }
  if name not in Users:
    return "User not found"
  else:
    return str(Users[name])



if __name__ == '__main__':
  app.run(debug=True)




from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = [{"firstname":"a",
"lastname":"b",
"email":"@mail.com",
"countries":"countries",
"contactnumber":"123",
"password":"password",
"commitment":3}]

companies = [
  {
    "companyname":"Microsoft",
    "role":"Data Engineer",
    "commitment":3
  }
]

@app.route("/form")
def signupform():
    return render_template('start.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    user = {"firstname": request.form['firstname'],
    "lastname": request.form['lastname'],
    "email": request.form["email1"],
    "countries": request.form['countries'],
    "contactnumber": request.form['contactnumber'],
    "password": request.form["password1"],
    "commitment": request.form["commitment"]}
    global users
    users.append(user)
    return redirect('/data')

@app.route('/data')
def data():
      return render_template(
            'userdata.html', users=users)

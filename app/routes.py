from flask import Flask, render_template, request, redirect
from app import app
import pdb

# app = Flask(__name__)

users = [{"firstname":"a",
"lastname":"b",
"email":"@mail.com",
"countries":"countries",
"contactnumber":"123",
"password":"password",
"commitment":'3'}]

userInSession = {}

companies = [\
  {
    "companyname":"Microsoft",
    "industry":"business",
    "commitment":'3',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
   {
    "companyname":"Microsoft2",
    "industry":"business",
    "commitment":'3',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
   {
    "companyname":"Microsoft3",
    "industry":"business",
    "commitment":'3',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
   {
    "companyname":"Microsoft4",
    "industry":"business",
    "commitment":'4',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
]

@app.route("/")
def index():
    return render_template('welcome.html')

@app.route("/form")
def signupform():
    return render_template('start.html')

@app.route("/")
def signupform2():
    return render_template('welcome.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    user = {
    "name": request.form["name"],
    "email": request.form["email1"],
    "countries": request.form['countries'],
    "contactnumber": request.form['contactnumber'],
    "password": request.form["password1"],
    "commitment": request.form["commitment"],
    "industry": request.form["industry"]
    }
    global users
    global userInSession
    users.append(user)
    userInSession = user
    return redirect('/result')

@app.route('/result')
def result():
    filteredCompanies = []
    global companies
    # pdb.set_trace()
    try:
        for company in companies:
            if company['commitment'] <= userInSession['commitment']\
            and company['industry'] == userInSession['industry']\
            and company['country'] == userInSession['countries']:
                filteredCompanies.append(company)
    except:
        return redirect('/form')
    return render_template('result.html', companies=filteredCompanies)


@app.route('/userdata')
def data():
      return render_template(
            'userdata.html', users=users)

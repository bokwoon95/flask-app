from flask import Flask, render_template, request, redirect
import pdb

app = Flask(__name__)

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
    "industry":"Tech",
    "commitment":'3',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
   {
    "companyname":"Microsoft2",
    "industry":"Tech",
    "commitment":'3',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
   {
    "companyname":"Microsoft3",
    "industry":"Tech",
    "commitment":'3',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
   {
    "companyname":"Microsoft4",
    "industry":"Tech",
    "commitment":'4',
    "country": "Cambodia",
    "description":"code things",
    "companynumber":"12345678",
  },
]

@app.route("/form")
def signupform():
    return render_template('start.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    user = {
    "name": request.form["name"],
    "email": request.form["email1"],
    "countries": request.form['countries'],
    "contactnumber": request.form['contactnumber'],
    "password": request.form["password1"],
    "commitment": request.form["commitment"]}
    global users
    global userInSession
    users.append(user)
    userInSession = user
    return redirect('/result')

@app.route('/result')
def result():
    filteredCompanies = []
    global companies
    for company in companies:
        if company['commitment'] <= userInSession['commitment']\
        and company['country'] == userInSession['countries']:
        # and company['industry'] == userInSession['industry']
            filteredCompanies.append(company)
        filteredCompanies.append(company)
    return render_template('result.html', companies=filteredCompanies)


@app.route('/userdata')
def data():
      return render_template(
            'userdata.html', users=users)

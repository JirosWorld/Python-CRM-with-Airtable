from flask import Flask, render_template, redirect, url_for, request
import config
import requests
import json


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

xheaders = { 'authorization': 'Bearer {}'.format(app.config['AIRTABLE_KEY']), 'content-type': 'application/json' }


@app.route('/')
def index():
    return render_template('index.html', **locals())

@app.route('/users', methods=["GET", "POST"])
def users():
    url = 'https://api.airtable.com/v0/app4vQ4CtiTItA8Rn/Teams?maxRecords=15'
    r = requests.get(url, headers=xheaders)
    result = json.loads(r.text)
    # print(result['records'])

    if request.method == 'POST':
        payload = {
            "records": [
                {
                    "fields": {
                        "teamId": request.form['teamId'],
                        "FirstName": request.form['FirstName'],
                        "LastName": request.form['LastName'],
                        "JobTitle": request.form['JobTitle'],
                        "Email": request.form['Email'],
                        "PhoneNumber": request.form['PhoneNumber'],
                        "ProfileImage": [{"url": request.form['ProfileImage']}],
                    }
                }
            ]
        }
        requests.post(
            "https://api.airtable.com/v0/app4vQ4CtiTItA8Rn/Teams",
            json=payload,
            headers=xheaders,
        )
        print(payload)
        return redirect(url_for('users'))

    return render_template('users.html', **locals())


@app.route('/leads')
def leads():
    url = 'https://api.airtable.com/v0/app4vQ4CtiTItA8Rn/Lead?maxRecords=10'
    r = requests.get(url, headers=xheaders)
    result = json.loads(r.text)
    # print(result['records'])
    return render_template('leads.html', **locals())


# 
# extra, unused templates for now
@app.route('/blank')
def blank():
    return render_template('blank.html', **locals())
    
@app.route('/buttons/')
def buttons():
    return render_template('buttons.html', **locals())

@app.route('/cards/')
def cards():
    return render_template('cards.html', **locals())

@app.route('/charts')
def charts():
    return render_template('charts.html', **locals())
    
@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html', **locals())

@app.route('/login')
def login_page():
    return render_template('login.html', **locals())

@app.route('/register')
def register_page():
    return render_template('register.html', **locals())
    
@app.route('/tables')
def tables():
    return render_template('tables.html', **locals())

@app.route('/utilities-animation')
def utilities_animation():
    return render_template('utilities-animation.html', **locals())

@app.route('/utilities-border')
def utilities_border():
    return render_template('utilities-border.html', **locals())

@app.route('/utilities-color')
def utilities_color():
    return render_template('utilities-color.html', **locals())

@app.route('/utilities-other')
def utilities_other():
    return render_template('utilities-other.html', **locals())

#  keep this at the end of the file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

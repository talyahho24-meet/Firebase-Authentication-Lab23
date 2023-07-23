from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {"apiKey": "AIzaSyDmQLDdOvWTq8GyIHH-ztMxio5IARiR-ww",
  "authDomain": "feivel-ef716.firebaseapp.com",
  "projectId": "feivel-ef716",
  "storageBucket": "feivel-ef716.appspot.com",
  "messagingSenderId": "480399213624",
  "appId": "1:480399213624:web:0da0df2dbe4ce3a8ed12cd",
  "measurementId": "G-5PNVEHC4VW"}

  firebase = pyrebase.initialize_app(config)
  auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)
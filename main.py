import pymysql
from flask import Flask, request, redirect, render_template,jsonify
from chat import get_response 
import re
# import mysql.connector


# Connect to the database
conn = pymysql.connect(host="localhost", user="root", password="123", db="re")

# Create the Flask app
app = Flask(__name__)

# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    msg=''
    if request.method == "POST":
        # Get the user inputs
        username = request.form["username"]
        password = request.form["password"]
        account={}
        # Verify the inputs
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM acc WHERE username=%s", (username,))
        account=cursor.fetchone()
        data=account[3]
        if data=='admin':
         if account[0]==username and account[1]==password:           
            return render_template("admin.html")
         else:
            msg='incorrect pswd'
            return render_template('login.html',msg=msg)
        else:
            if account[0]==username and account[1]==password:
               return render_template("index.html")
            else:
               msg='incorrect pswd'
               return render_template('login.html',msg=msg)
    return render_template("login.html")

@app.route('/register', methods =['GET', 'POST'])
def register():
 msg = ''
 if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
  username = request.form['username']
  password = request.form['password']
  email = request.form['email']
  type ='user'
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM acc WHERE username = % s', (username ))
  account = cursor.fetchone()
  if account:
   msg = 'Account already exists !'
  elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
   msg = 'Invalid email address !'
  elif not re.match(r'[A-Za-z0-9]+', username):
   msg = 'Username must contain only characters and numbers !'
  elif not username or not password or not email:
   msg = 'Please fill out the form !'
  else:
    cursor.execute('INSERT INTO acc VALUES ( % s, % s, % s, % s)', (username, password,email,type,))
    cursor.connection.commit()
    msg = 'You have successfully registered !'
    return render_template('login.html')
 elif request.method == 'POST':
  msg = 'Please fill out the form !'
 return render_template('register.html', msg = msg)
@app.route('/campus')
def campus():
    return render_template("campus.html")
@app.route('/athletics')
def athletics():
    return render_template("athletics.html")     
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/enquries',methods=["GET", "POST"])
def enquries():
    if request.method == "POST":
        # Get the user inputs
        username = request.form["username"]
        # password = request.form["password"]
        account={}

        # Verify the inputs
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM acc WHERE username=%s", (username,))
        account=cursor.fetchone()
        if account:
            return redirect("index_get")
        else:
            return render_template("login.html")
    return render_template("enquries.html")
@app.route('/base')
def base():
    return render_template("base.html")
@app.route('/notice')
def notice():
    return render_template("notice.html")
@app.route('/index_get')
def index_get():
    return render_template("base.html")
@app.route('/library')
def library():
    return render_template("library.html")
@app.route('/courses')
def courses():
    return render_template("courses.html")
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/ai')
def ai():
    return render_template("ai.html")
@app.route('/research')
def research():
    return render_template("research.html")
@app.route('/researchapply', methods =['GET', 'POST'])
def researchapply():
    if request.method == 'POST' and 'fullname' in request.form and 'address' in request.form and 'phonenumber' in request.form and 'subject' in request.form:
       fullname = request.form['fullname']
       address = request.form['address']
       phonenumber = request.form['phonenumber']
       subject = request.form['subject']
       cursor = conn.cursor()
       cursor.execute('INSERT INTO rsp VALUES ( % s, % s, % s, %s )', (fullname,address,phonenumber,subject,))
       cursor.connection.commit()
    return render_template('researchapply.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        text=request.get_json().get("message")
        response =get_response(text)
        message ={"answer":response}
        return jsonify(message)
@app.route('/review',methods=['GET','POST'])
def review():
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM acc")
     data=cursor.fetchall()
     print(type(data[0]))
     cursor.close()
     return render_template('loginandreview.html',data=data)
@app.route('/admission')
def admission():
   return render_template('admission.html')
@app.route('/admissionadd',methods =['GET', 'POST'])
def admisionadd():
    fullname = request.form['fullname']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    phonenumber = request.form['phonenumber']
    course = request.form['Course']
    cursor = conn.cursor()
    cursor.execute('INSERT INTO adii VALUES ( % s, % s, % s, %s, %s, %s )', (fullname,address,city,state,phonenumber,course,))
    cursor.connection.commit()
    return render_template('index.html')
   

@app.route('/admissiondetails',methods=['GET','POST'])
def admissiondetails():
     cursor = conn.cursor()
     cursor.execute("select*from adii")
     data=cursor.fetchall()
     cursor.close()
     return render_template('admissionandview.html',data=data)
@app.route('/contact', methods =['GET', 'POST'])
def contact():
 msg = ''
 if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'phonenumber' in request.form and 'message' in request.form:
  name = request.form['name']
  email = request.form['email']
  phonenumber = request.form['phonenumber']
  message = request.form['message']
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM cc WHERE name = % s', (name, ))
  account = cursor.fetchone()
  if account:
   msg = 'Account already exists !'
  else:
    cursor.execute('INSERT INTO cc VALUES ( % s, % s, % s, %s )', (name,email,phonenumber,message))
    cursor.connection.commit()
    msg = 'You have successfully registered !'
    return render_template('contact.html')
 elif request.method == 'POST':
  msg = 'Please fill out the form !'
 return render_template('contact.html', msg = msg)
@app.route('/contactrev',methods=['GET','POST'])
def contactrev():
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM cc")
     data=cursor.fetchall()
    
     cursor.close()
     return render_template('contactrev.html',data=data)

@app.route('/researchview',methods=['GET','POST'])
def researchview():
     cursor = conn.cursor()
     cursor.execute("select*from rsp")
     data=cursor.fetchall()
     print(data)
     cursor.close()
     return render_template('researchview.html',data=data)

@app.route('/bl', methods =['GET','POST'])
def bl():
    if request.method == 'POST' and 'name' in request.form and 'age' in request.form and 'bloodgroup' in request.form and 'place' in request.form and 'phonenumber' in request.form:
       name = request.form['name']
       age = request.form['age']
       bloodgroup = request.form['bloodgroup']
       place = request.form['place']
       phonenumber = request.form['phonenumber']
       cursor = conn.cursor()
       cursor.execute('INSERT INTO blo VALUES ( % s, % s, % s, %s, %s )', (name,age,bloodgroup,place,phonenumber))
       cursor.connection.commit()
    return render_template('bl.html')

@app.route('/blview',methods=['GET','POST'])
def blview():
     cursor = conn.cursor()
     cursor.execute("select*from blo")
     data=cursor.fetchall()
     print(data)
     cursor.close()
     return render_template('blview.html',data=data)


if __name__=="__main__":
    app.run(debug=True)
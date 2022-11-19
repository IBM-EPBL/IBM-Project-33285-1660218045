from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re
from datetime import datetime


app = Flask(__name__)
  
app.secret_key = 'a'

#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31929;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xlv63468;PWD=WmfPc96bnmmg6WJ9",'','')
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=31249;SECURITY=SSL;SSLSererCertificate=DigiCertGlobalRootCA.crt;UID=rzl30414;PWD=osIBVZs3TTylNYFp",'','')

@app.route('/')

def homer():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')
@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
    session_name = ''
    username = ''
    if request.method == 'POST' :
        username = request.form['email']
        password = request.form['pass']
        sql = "SELECT * FROM signup WHERE EMAIL =? AND PASSWORD=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['EMAIL']
            userid=  account['EMAIL']
            session['username'] = account['EMAIL']
            msg = 'Logged in successfully !'
            name = account['NAME']
            email = account['EMAIL']
            number =  account['PHONE']
            now = datetime.now()
            insert_sql = "INSERT INTO  session VALUES (?, ?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name )
            ibm_db.bind_param(prep_stmt, 2, email )
            ibm_db.bind_param(prep_stmt, 3, number)
            ibm_db.bind_param(prep_stmt, 4, now)
            ibm_db.execute(prep_stmt)
            return render_template('user.html', msg = msg)
        else:
            msg = 'Incorrect username or password !'
    return render_template('login.html', msg = msg)

        

   
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['pass']
        sql = "SELECT * FROM SIGNUP WHERE EMAIL =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        else:
            insert_sql = "INSERT INTO  signup VALUES (?, ?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, username)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, phone)
            ibm_db.bind_param(prep_stmt, 4, password)
            ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered!'
            return render_template('login.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)


@app.route('/session')
def session():
    sql = "SELECT * FROM  SESSION"
    stmt = ibm_db.exec_immediate(conn,sql)
    acnt = []
    abc = ibm_db.fetch_assoc(stmt)
    while abc!=False:
        account = abc
        acnt.append(account)
        abc = ibm_db.fetch_assoc(stmt)
    return render_template('session.html',account=acnt)

@app.route('/dashboard')
def dash():
    return render_template('admin_dashboard.html')

@app.route('/today_offers')
def today_offers():
    return render_template('today_offers.html')

@app.route('/stock')
def stock():
    sql = "SELECT * FROM  dress_details"
    stmt = ibm_db.exec_immediate(conn,sql)
    acnt = []
    abc = ibm_db.fetch_assoc(stmt)
    while abc!=False:
        account = abc
        acnt.append(account)
        abc = ibm_db.fetch_assoc(stmt)
    #return render_template('session.html',)
    return render_template('stock_details.html',account=acnt)

@app.route('/apply',methods =['GET', 'POST'])
def apply():
     msg = ''
     if request.method == 'POST' :
         username = request.form['username']
         email = request.form['email']
         
         qualification= request.form['qualification']
         skills = request.form['skills']
         jobs = request.form['s']
         sql = "SELECT * FROM users WHERE username =?"
         stmt = ibm_db.prepare(conn, sql)
         ibm_db.bind_param(stmt,1,username)
         ibm_db.execute(stmt)
         account = ibm_db.fetch_assoc(stmt)
         print(account)
         if account:
            msg = 'there is only 1 job position! for you'
            return render_template('apply.html', msg = msg)

         
         
         insert_sql = "INSERT INTO  job VALUES (?, ?, ?, ?, ?)"
         prep_stmt = ibm_db.prepare(conn, insert_sql)
         ibm_db.bind_param(prep_stmt, 1, username)
         ibm_db.bind_param(prep_stmt, 2, email)
         ibm_db.bind_param(prep_stmt, 3, qualification)
         ibm_db.bind_param(prep_stmt, 4, skills)
         ibm_db.bind_param(prep_stmt, 5, jobs)
         ibm_db.execute(prep_stmt)
         msg = 'You have successfully applied for job !'
         session['loggedin'] = True
         TEXT = "Hello sandeep,a new appliaction for job position" +jobs+"is requested"
         
         #sendmail(TEXT,"sandeep@thesmartbridge.com")
         sendgridmail("sandeep@thesmartbridge.com",TEXT)
         
         
         
     elif request.method == 'POST':
         msg = 'Please fill out the form !'
     return render_template('apply.html', msg = msg)

@app.route('/display')
def display():
    print(session["username"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM job WHERE userid = % s', (session['id'],))
    account = cursor.fetchone()
    print("accountdislay",account)

    
    return render_template('display.html',account = account)

@app.route('/logout')

def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('home.html')


    
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)

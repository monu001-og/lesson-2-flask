from flask import   Flask,render_template,request
import mysql.connector
import re

app=Flask(__name__)

@app.route('/login' , methods =['GET','POST'])
def login():
    msg=''
    if request.method =='POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(host="d4bfree.net",
                                       user="rootcodingal_123"
                                       password="root1234"
                                       database="students123")
        mycursor = mydb.cursor()
        mycursor.execute(
            'SELECT * FROM LoginDetails WHERE username = %s AND password =%s',(username,password)
        )
        account=mycursor.fetchone()
        if account:
            print('login success')
            name=account[1]
            id=account[0]
            msg='Logged in Succcessfully'
            print('login successfull')
            return render_template("index.html",msg=msg , name=name ,id=id)
        else:
            msg='incorrect'
            return render_template('login.html')
        
        
@app.route('/logout')
def logout():
    name='
    id=''
    msg='logeed out successfully'
    return render_template('login.html',msg=msg,name=name,id=id)
    
@app.route('/register' , methods =['GET','POST'])
def register():
    msg=''
    if request.method =='POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email=request.form['email']
        mydb = mysql.connector.connect(host="d4bfree.net",
                                       user="rootcodingal_123"
                                       password="root1234"
                                       database="students123")
        mycursor = mydb.cursor()
        mycursor.execute(
            'SELECT * FROM LoginDetails WHERE username = %s AND email =%s',(username,email)
        )
        account=mycursor.fetchone()
        print(account)
        if account:
            msg='Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+'email):
            msg='Invalid email address'
        
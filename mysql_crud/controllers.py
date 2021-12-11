from flask import Flask, render_template, request, redirect
from db import mydb, mycursor
import string
import random

app = Flask(__name__)
username = "admin"
password = "admin101"

size= 2000
randomlink = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
randomString = str(randomlink)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM user")
    user = mycursor.fetchall()
    return render_template('index.html', user = user)

@app.route('/home', methods = ["GET", "POST"])
def home_view():
    message =''
    if request.method == 'GET':
        return render_template("admin_cont.html")
    if request.method == "POST" :
        _name = request.form['username']
        _password = request.form['password']
        if _name==username and _password==password:
            return redirect(f'/records')
        else :
            message = "Invalid credentials"
    return render_template("admin_cont.html" , msg =message)

@app.route('/records')
def records():
    mycursor.execute('SELECT * FROM user')
    users = mycursor.fetchall()
    return render_template("records.html", users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_users():
    if request.method == 'GET':
        return render_template('post_form.html')
    if request.method == 'POST':
        _name = request.form['name']
        _email = request.form['email']
        _phonenumber = request.form['phonenumber']
        _date1 = request.form['date1']
        _date2 = request.form['date2']
        sql = 'INSERT INTO user (name, email, phonenumber, date1, date2) VALUES (%s, %s, %s, %s, %s)'
        val = (_name, _email, _phonenumber, _date1, _date2)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/records')



@app.route('/details/<int:id>')
def users_details(id):
    mycursor.execute(f'SELECT * FROM user WHERE ID={id}')
    users = mycursor.fetchone()
    return render_template('users_detail.html', users = users)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_users(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM user WHERE ID={id}')
        users = mycursor.fetchone()
        return render_template('edit_users.html', users = users)
    if request.method == 'POST':
        _name = request.form['name']
        _email = request.form['email']
        _phonenumber = request.form['phonenumber']
        _date1 = request.form['date1']
        _date2 = request.form['date2']
        sql = f'UPDATE user SET name = %s, email = %s, phonenumber = %s, date1 = %s, date2 = %s WHERE ID = %s'
        values = (_name, _email, _phonenumber, _date1, _date2, id)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('/')


@app.route('/delete/<int:id>')
def delete_users(id):
    sql = f'DELETE FROM user WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/records')


if __name__ == '__main__':
    app.run()
import os
import mysql.connector
from werkzeug.security import generate_password_hash
from flask import Flask, render_template, request, redirect, url_for
from forms import SignUpForm, addBook

app = Flask(__name__)

def create_connection():
    db = mysql.connector.connect(
        host = 'abram0vych.mysql.pythonanywhere-services.com',
        user = 'abram0vych',
        password = 'qE09#Za79Zff',
        database = 'abram0vych$library')
    return db

def close_connection(db):
    db.close()

def get_books():
    mydb = create_connection()
    mycursor = mydb.cursor()
    sql_txt = "SELECT * FROM T_books"
    mycursor.execute(sql_txt)
    myresult = mycursor.fetchall()
    close_connection(mydb)
    return myresult

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/endurance')
def endurance():
    return render_template('endurance.html')

@app.route('/james_caird')
def james_caird():
    return render_template('james_caird.html')

@app.route('/books')
def books():
    books = get_books()
    return render_template('books.html',books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = addBook(request.form)
    if request.method == 'POST' and form.validate():
        mydb = create_connection()
        mycursor = mydb.cursor()
        sql_txt = "INSERT INTO T_books (ISBN, title, author) VALUES ('" + form.ISBN.data + "', '" + form.title.data + "','" + form.author.data + "')"
        mycursor.execute(sql_txt)
        mydb.commit()
        close_connection(mydb)
        books = get_books()
        return redirect('/books')
    return render_template('add_book.html',form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        mydb = create_connection()
        mycursor = mydb.cursor()
        sql_txt = "INSERT INTO users (fname, surname, email, password, code) VALUES ('" + form.fname.data + "', '" + form.surname.data + "','" + form.email.data + "', '" + generate_password_hash(form.password.data) + "', '" + form.code.data + "')"
        mycursor.execute(sql_txt)
        mydb.commit()
        close_connection(mydb)
        return render_template('display.html',form=form)
    return render_template('signup.html',form=form)

if __name__ == '__main__':
    app.run(DEBUG = True)
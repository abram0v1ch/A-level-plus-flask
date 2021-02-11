import mysql.connector

def create_connection():
    db = mysql.connector.connect(
        host = 'abram0vych.mysql.pythonanywhere-services.com',
        user = 'abram0vych',
        password = 'qE09#Za79Zff',
        database = 'abram0vych$library')
    return db

def close_connection(db):
    db.close()

def create_book_table():
    mydb = create_connection()
    mycursor = mydb.cursor()
    sql_txt = 'CREATE TABLE T_books (ISBN VARCHAR(25) NOT NULL PRIMARY KEY, title VARCHAR(55), author VARCHAR(55))'
    mycursor.execute(sql_txt)
    close_connection(mydb)

def create_users_table():
    mydb = create_connection()
    mycursor = mydb.cursor()
    sql_txt = 'CREATE TABLE users (ID int NOT NULL PRIMARY KEY, fname VARCHAR(30), surname VARCHAR(30), email VARCHAR(30), password VARCHAR(200), code VARCHAR(10))'
    mycursor.execute(sql_txt)
    close_connection(mydb)

def add_book(isbn, title, author):
    mydb = create_connection()
    mycursor = mydb.cursor()
    sql_txt = "INSERT INTO T_books (ISBN, title, author) VALUES ('" + isbn + "', '" + title + "','" + author + "')"
    mycursor.execute(sql_txt)
    mydb.commit()
    close_connection(mydb)

def get_books():
    mydb = create_connection()
    mycursor = mydb.cursor()
    sql_txt = "SELECT * FROM T_books"
    mycursor.execute(sql_txt)
    myresult = mycursor.fetchall()
    close_connection(mydb)
    return myresult

def get_users():
    mydb = create_connection()
    mycursor = mydb.cursor()
    sql_txt = "SELECT * FROM users"
    mycursor.execute(sql_txt)
    myresult = mycursor.fetchall()
    close_connection(mydb)
    return myresult

users = get_users()
print(users)
#create_users_table()
# add_book("9781853260285","Emma","Jane Austin")
# books = get_books()
# print(books)
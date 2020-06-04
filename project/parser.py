from flask import Flask, render_template,flash , redirect, url_for,session, logging, request, session
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import sqlite3
import json



app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="D@nil@2001"
app.config['MYSQL_DB']="myflaskapp"
app.config['MYSQL_CURSORCLASS']="DictCursor"
# init MYSQL
mysql=MySQL(app)

def parser(name):
  with open(name, encoding='UTF-8') as f:
    js = json.load(f)
    cur = mysql.connection.cursor()
    for name in js:
      films = list(js[name].values())
      try:
        las="INSERT INTO films (nam, year, country, producer, duration, rating, theaters, dates, tim, descript) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"  
        val = (films[0],films[1],films[2],films[3],films[4],films[5],films[6],films[7],films[8],films[9] )
        cur.execute(las,val)
                #post = films(name=name, year=films[0], country=films[1], producer=films[2], duration=films[3],
                              #rating=films[4],
                              #theaters=films[5], dates=films[6], time=films[7], description=films[8], image=films[9],
                              #genre=films[10])
            

      #close con
      except IntegrityError:
        print(f"Фильм {name} уже в базе данных.")
    mysql.connection.commit()
    cur.close()

parser('Movie_sessions_parser.json')
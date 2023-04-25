#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="app",
  password="1234",
  database="todo_list"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE if not exists customers (name VARCHAR(255), address VARCHAR(255))")
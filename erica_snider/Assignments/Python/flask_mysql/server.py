from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb1')
# an example of running a query
# print mysql.query_db("INSERT INTO users (name) VALUES ('Bob')")
print mysql.query_db("SELECT * FROM users")
app.run(debug=True)

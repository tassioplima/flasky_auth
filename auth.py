from flask import Flask
from flask_sqlalchemy import SQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/api_example/todo.db'

db = SQLAlchemy(app)

if __name__== '__main__':
    app.run(debug=True)

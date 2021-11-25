from flask import Flask, jsonify, request
from flask_sqlalchemy import abort
from model import *
from dotenv import load_dotenv
import os

# Loading in credentials from a .env file (you could just as easily
# directly set each variable to its corresponding value below)
load_dotenv()
user_name = os.environ.get('DATABASE_USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
database = os.environ.get('DATABASE')


# Initializing the application
app = Flask(__name__)

# Connecting to the postgres server
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_name}:{password}@{host}:5432/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connecting the db with the application
db.init_app(app)

# Starting working on routes


@app.route('/')
def index():
    return 'Hello World!'

# This is a decorator to read more about this check this link:
# https://realpython.com/primer-on-python-decorators/#simple-decorators


@app.route('/api/article', methods=['GET'])
def getArticles():
    # This function is run when this api route is called
    try:
        # Getting all the articles from database using SQLAlcemy
        data = Articles.query.all()

        # Since we now have all articles as objects we need to convert them
        # into a form that we can use to transfer data to the frontend
        article = [article.serialize() for article in data]

        # Returning JSON data
        return jsonify({
            "success": True,
            "articles": article
        })

    except BaseException:
        # This method is used to abort send a error message
        # Note that this is NOT good error checking, you should be returning different error codes depending on
        # what happens. (ex. sending a 400 if the user sent over 'bad' data to the endpoint)
        # Here for the workshop we just catch all the erros and return a 500 (internal server error) code
        abort(500)


@app.route('/api/article/<int:id>', methods=['GET'])
def getArticle(id):
    try:
        article = Articles.query.filter_by(id=id).first()
        return jsonify({
            "success": True,
            "articles": article.serialize()
        })
    except BaseException:
        # you ideally would want to do more error checking than this
        abort(500)


@app.route('/api/article', methods=['POST'])
def addArticle():
    details = request.get_json()
    print(details)
    try:
        article = Articles(
            details["title"], details["body"], details["author"])
        db.session.add(article)
        db.session.commit()
        return jsonify({
            "success": True,
            "articles": article.serialize()
        })
    except BaseException:
        # you ideally would want to do more error checking than this
        abort(500)


@app.route('/api/article/<int:id>', methods=['PUT'])
def editArticle(id):
    details = request.get_json()
    article = None
    try:
        article = Articles.query.filter_by(id=id).first()
        if "title" in details:
            article.title = details['title']
        if "body" in details:
            article.body = details['body']
        db.session.commit()
    except BaseException:
        # you ideally would want to do more error checking than this
        abort(500)

    if article:
        return jsonify({
            "success": True,
            "articles": article.serialize()
        })
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_sqlalchemy import abort
from model import *
from dotenv import load_dotenv
import os

# Getting credentials
load_dotenv()
user_name = os.environ.get('DATABASE_USER')
password = os.environ.get('PASSWORD')
database = os.environ.get('DATABASE')

# Initializing the application
app = Flask(__name__)
# Connecting to the postgres server
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_name}:{password}@{database}:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# connecting the db with the application
db.init_app(app)

# Starting working on routes
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/get-all-articles', methods=['GET'])
def getArticles():
    try:
        a = Articles.query.all()
        a = [art.serialize() for art in a]
        return jsonify({
                "success": True,
                "articles": a
            })
    except BaseException:
        abort(422)

@app.route('/get-article/<int:id>', methods=['GET'])
def getArticle(id):
    try:
        a = Articles.query.filter_by(id=id).first()
        return jsonify({
                "success": True,
                "articles": a.serialize()
            })
    except BaseException:
        abort(422)
    

@app.route('/add-article', methods=['POST'])
def addArticle():
    details = request.get_json()
    try:
        article = Articles(details["title"], details["body"], details["author"])
        db.session.add(article)
        db.session.commit()
        return jsonify({
                "success": True,
                "articles": article.serialize()
            })
    except BaseException:
        abort(422)

@app.route('/article/<int:id>', methods=['PUT'])
def editArticle(id):
    details = request.get_json()
    a = None
    try:
        a = Articles.query.filter_by(id=id).first()
        if "title" in details:
            a.title = details['title']
        if "body" in details:
            a.body = details['body']
        db.session.commit()
    except BaseException:
        abort(422)
    if a:
        return jsonify({
                "success": True,
                "articles": a.serialize()
            })
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)

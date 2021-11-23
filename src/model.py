from typing import NoReturn
from sqlalchemy import Column, Text, VARCHAR, BigInteger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import Integer

db = SQLAlchemy()

class Articles(db.Model):
    __tablename__ = 'Articles'

    id = Column(BigInteger().with_variant(Integer, 'postgresql'), primary_key=True)
    title = Column(VARCHAR(100), nullable=False)
    body = Column(Text())
    author = Column(VARCHAR(35))


    def __init__(self, id, title, body, author):
        self.id = id
        self.title = title
        self.body = body
        self.author = author

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            "author": self.author
        }
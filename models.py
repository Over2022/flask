from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    comments = relationship("Comment", back_populates="parent_post")

    def __repr__(self):
        return '<Article %r>' % self.id


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    parent_post = relationship("Article", back_populates="comments")
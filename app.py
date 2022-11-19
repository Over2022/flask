from flask import Flask
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, defult=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Strting(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DataTime, defult=datetime.utcnow)




@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page:' + name + '-' + str(id)


if __name__ == '__main__':
    app.run(debug=True)
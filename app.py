from flask import Flask, request, redirect
from flask import render_template
from models import db, Article, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db.init_app(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/posts/<int:id>')
def article(id):
    article = Article.query.get(id)
    return render_template('article.html', article=article)


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date).all()
    # comments = Comment.query.all()
    return render_template('posts.html', articles=articles)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/comment/<int:post_id>', methods=['GET', 'POST'])
def comment(post_id):
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']

        comment = Comment(name=name, text=text, post_id=post_id)
        try:
            db.session.add(comment)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При добавлении комментария возникла ошибка'
    else:
        return render_template('comment.html')


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При добавлении статьи произошла ошибка'

    else:
        return render_template('create-article.html')


@app.route('/create')
def create():
    db.create_all()
    return 'All tables created'


if __name__ == '__main__':
    app.run(debug=True)
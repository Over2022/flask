from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return 'HELLO'


@app.route('/about')
def about():
    name = 'Alesya?'
    NameList = [q for q in name if q.isalpha()]
    NameList.reverse()
    return ''.join(NameList)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'User page' + name + '-' + id


if __name__ == '__main__':
    app.run(debug=True)
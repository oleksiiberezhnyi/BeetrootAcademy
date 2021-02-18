from flask import Flask, request, render_template, session, redirect, url_for, flash
from datetime import datetime
import time
from werkzeug.security import generate_password_hash, check_password_hash
import json
from flask_sqlalchemy import SQLAlchemy


class Style:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Error:

    def __init__(self, code: int):
        self.code = code
        self.error()

    def error(self):
        error = {'error': {'code': self.code}}
        return error

    def __repr__(self):
        return f'dict("error"= ("code"= {self.code})'

app = Flask(__name__)
app.config['SECRET_KEY'] = b'sadlkgsalei8012935yhefmkz;dutr823'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    message = db.Column(db.Text, nullable=False)
    user_name = db.Column(db.String(20), nullable=False, default='ANON')

    def __repr__(self):
        return f'<Message {self.id}>'


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_password = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<User {self.user_id}>'


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    try:
        if session['user_name']:
            user_name = session['user_name']
            user = User.query.filter_by(user_name=user_name).first()
            if request.method == 'POST':
                try:
                    message = Message(
                        message=request.form['message'],
                        date=datetime.utcnow().strftime('[%Y-%m-%d %H:%M:%S]'),
                        user_name=user.user_name
                    )
                    db.session.add(message)
                    db.session.commit()
                    flash('Повідомлення надіслано')
                    return redirect(url_for('chat'))
                except:
                    flash('При відправці повідомлення виникла невідома помилка')
                    time.sleep(1)
                    return redirect(url_for('chat'))
            else:
                messages = Message.query.order_by(Message.date.desc()).all()
            return render_template('chat.html', messages=messages, user_name=user_name)
    except:
        if request.method == 'POST':
            return redirect(url_for('login'))
        return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    session.pop('user_name', None)
    session.pop('_flashes', None)
    if request.method == 'POST':
        if len(User.query.filter_by(user_name=request.form['user_name']).all()) == 0:
            flash(f'Користувача {request.form["user_name"]} не існує. Зараз ви перейдете на сторінку реєстрації')
            time.sleep(2)
            return redirect(url_for('register'))
        else:
            user = User.query.filter_by(user_name=request.form['user_name']).first()
            if 'user_name' in session:
                return redirect(url_for('chat'))
            elif request.form['user_name'] == user.user_name \
                    and check_password_hash(user.user_password, request.form['password']):
                session['user_name'] = user.user_name
                return redirect(url_for('chat'))
            else:
                flash('Ви ввели не правильний пароль!')
                time.sleep(1)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if len(User.query.filter_by(user_name=request.form['user_name']).all()) > 0:
            flash(f'Користувач {request.form["user_name"]} існує')
        else:
            session.pop('_flashes', None)
            hash_password = generate_password_hash(request.form['password'])
            user = User(user_name=request.form['user_name'], user_password=hash_password)
            session['user_name'] = user.user_name
            try:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('chat'))
            except:
                return redirect(url_for('register'))
    return render_template('register.html')


if __name__ == '__main__':
    def run_app():
        app.run(debug=True)

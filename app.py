from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'your-secret-key'

UPLOAD_FOLDER = 'static/uploads'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aldrin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)  
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    image_filename = db.Column(db.String(), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    address = db.Column(db.String(), nullable=True)

def calculate_age(birthday):
    if not birthday:
        return None
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        birthday_str = request.form['birthday']
        address = request.form['address']
        image = request.files['image']

        birthday = None
        try:
            birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
        except Exception:
            pass

        filename = None
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(f"{UPLOAD_FOLDER}/{filename}")

        new_user = User(
            name=name,
            username=username,
            password=password,
            birthday=birthday,
            address=address,
            image_filename=filename
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception:
            db.session.rollback()
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username, password=password).first()
    if user:
        session['user_id'] = user.id
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    user = User.query.get(user_id)
    if not user:
        return redirect(url_for('login'))

    age = calculate_age(user.birthday)
    return render_template('profile.html', user=user, age=age)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

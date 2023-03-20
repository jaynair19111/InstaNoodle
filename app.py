from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noodle.db'
db = SQLAlchemy(app)

class Noodle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    spice = db.Column(db.Integer, unique=False, nullable=False)
    sodium = db.Column(db.Integer, unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)

@app.route('/')
def index():
    noodles = Noodle.query.all()
    return render_template('noodles.html', noodles=noodles, url_for=url_for)

@app.route('/add', methods=['GET', 'POST'])
def add_noodle():
    if request.method == 'POST':
        image = request.form['image']
        name = request.form['name']
        description = request.form['description']
        spice = request.form['spice']
        sodium = request.form['sodium']
        price = request.form['price']

        noodle = Noodle(image=image, name=name, description=description, spice=spice, sodium=sodium, price=price)
        db.session.add(noodle)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_noodle.html')
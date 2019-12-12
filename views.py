#modules-------------------------
from app import app, db
from models import Restaurants
from models import Reservations
from forms import BookForm

#libraries-----------------------
from flask import render_template, request
import random
import string
from passlib.hash import sha256_crypt


def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

"""@app.route("/", methods=["GET", "POST"])
def home():
    reservations = Reservations.query.all()
    if request.method == "POST":
        if 'add' in request.form:
            res_day = Reservations(s_day=request.form.get("s_day"), s_r_id=request.form.get("s_r_id"))
            db.session.add(res_day)
            db.session.commit()
            print(request.form)
        elif 'show' in request.form:
            return render_template("home.html", reservations=reservations, toshow=True)
        elif 'hide' in request.form:
            return render_template("home.html", reservations=reservations, toshow=False)
    return render_template("home.html")"""

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/reservation/<string:id>", methods=["GET", "POST"])
def reservation(id):
    reservations = Reservations.query.filter(Reservations.s_r_id == id)
    for i in reservations:
        print(i)
    if request.method == "POST":
        if 'add' in request.form:
            res_day = Reservations(s_day=request.form.get("sday"), s_r_id=id)
            db.session.add(res_day)
            db.session.commit()
            print(request.form)
        elif 'show' in request.form:
            return render_template("reservation.html", reservations=reservations, toshow=True, id=id)
        elif 'hide' in request.form:
            return render_template("reservation.html", reservations=reservations, toshow=False, id=id)
    return render_template("reservation.html", id=id)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = sha256_crypt.hash(request.form["password"])
        name = request.form["rest_name"]
        address = request.form["rest_address"]
        owner_name = request.form["owner_name"]
        new_key = randomString(15)
        new_user = Restaurants(r_username=username, r_password=password, r_name=name, r_adress=address, r_ownername=owner_name, r_key=new_key)
        db.session.add(new_user)
        db.session.commit()
        app.logger.info("new user registered")
    return render_template("register.html")





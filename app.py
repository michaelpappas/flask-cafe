"""Flask App for Flask Cafe."""

from flask import Flask, render_template, redirect, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
import os
from forms import CafeForm, SignupForm, LoginForm

from models import db, connect_db, Cafe, City, User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flaskcafe'
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "shhhh")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

# toolbar = DebugToolbarExtension(app)

connect_db(app)

#######################################
# auth & auth routes

# CURR_USER_KEY = "curr_user"
# NOT_LOGGED_IN_MSG = "You are not logged in."


# @app.before_request
# def add_user_to_g():
#     """If we're logged in, add curr user to Flask global."""

#     if CURR_USER_KEY in session:
#         g.user = User.query.get(session[CURR_USER_KEY])

#     else:
#         g.user = None


# def do_login(user):
#     """Log in user."""

#     session[CURR_USER_KEY] = user.id


# def do_logout():
#     """Logout user."""

#     if CURR_USER_KEY in session:
#         del session[CURR_USER_KEY]


#######################################
# homepage

@app.get("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


#######################################
# cafes


@app.get('/cafes')
def cafe_list():
    """Return list of all cafes."""

    cafes = Cafe.query.order_by('name').all()

    return render_template(
        'cafe/list.html',
        cafes=cafes,
    )


@app.get('/cafes/<int:cafe_id>')
def cafe_detail(cafe_id):
    """Show detail for cafe."""

    cafe = Cafe.query.get_or_404(cafe_id)

    return render_template(
        'cafe/detail.html',
        cafe=cafe,
    )

@app.route('/cafes/add', methods=["GET", "POST"])
def add_cafe():
    """ Add a cafe. """

    form = CafeForm()

    # cities = [(city.code, city.name) for city in City.query.all()]
    # form.city.choices = cities
    form.city.choices = City.get_cities()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        url = form.url.data or None
        address = form.address.data
        city = form.city.data
        image = form.image.data or None

        new_cafe = Cafe(name=name,
                    description=description,
                    url=url,
                    address=address,
                    city_code=city,
                    image_url=image)

        db.session.add(new_cafe)
        db.session.commit()

        flash("New cafe has been added!")
        return redirect(f"/cafes/{new_cafe.id}")

    else:
        return render_template("/cafe/add-form.html", form=form)

@app.route('/cafes/<int:cafe_id>/edit', methods=["GET", "POST"])
def edit_cafe(cafe_id):
    """ Edit a cafe. """

    cafe = Cafe.query.get_or_404(cafe_id)
    form = CafeForm(obj=cafe)

    # cities = [(city.code, city.name) for city in City.query.all()]
    # form.city.choices = cities
    form.city.choices = City.get_cities()

    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.description = form.description.data
        cafe.url = form.url.data or None
        cafe.address = form.address.data
        cafe.city_code = form.city.data
        cafe.image = form.image.data or None

        db.session.commit()

        flash(f"{cafe.name} edited!")
        return redirect(f"/cafes/{cafe.id}")

    else:
        return render_template("/cafe/edit-form.html", form=form, cafe=cafe)

########################################## User Routes ############################

@app.route('/signup', methods=["GET", "POST"])
def user_signup():
    """ Show user signup form and POST form data """

    form = SignupForm

    if form.validate_on_submit():
        username = form.username.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        description = form.description.data
        email = form.email.data
        password = form.password.data
        image_url = form.image_url.data

        user = User.register(
                        username = username,
                        first_name = first_name,
                        last_name = last_name,
                        description = description,
                        email = email,
                        password = password,
                        image_url = image_url
        )

        db.session.add(user)
        db.session.commit()

        session["username"] = user.username

        flash("You are signed up and logged in.")

    else:
        return render_template('/auth/signup-form.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def user_login():
    """ Show user login form and POST form data """

    form = LoginForm

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

    user = User.login(username, password)


# web_app/routes/home_routes.py
from flask import Blueprint, render_template
from web_app.models import User
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():

    screen_names = User.query.with_entities(User.screen_name).distinct()
    for screen_name in screen_names:
        print(screen_name[0])
    # breakpoint()

    # FETCH USERS FROM DATABASE
    # breakpoint()




    return render_template("prediction_form.html", screen_names=screen_names)

@home_routes.route("/hello")
def hello():
    x = 2 + 2
    return f"About me {x}"
import requests
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    jsonify,
)
from flask_login import login_required, current_user


from scrapper import scraping, BeautifulSoup

main = Blueprint("main", __name__, template_folder="core/templates")


@main.route("/index", methods=["GET", "POST"])
@login_required
def index():

    return render_template("index.html")


@main.route("/scraping", methods=["GET", "POST"])
def scrap():
    if request.method == "GET":
        return redirect(url_for("main.index"))

    phones = scraping()

    return jsonify(
        {"htmlresponse": render_template("response.html", phones=phones)}
    )


@main.route("/image", methods=["POST"])
def get_image():
    if request.method == "GET":
        return redirect(url_for("main.index"))

    phone = request.form["link"]

    response = requests.get(phone)

    soup = BeautifulSoup(response.content, "html.parser")
    try:
        image = soup.select_one(".css-1bmvjcs")["src"].split(";")[0]
    except TypeError:
        image = "Image not Found"
    return jsonify({"image": image, "link": phone})


@main.route("/")
def home():
    if current_user.is_anonymous:
        return redirect(url_for("users.login"))
    return redirect(url_for("main.index"))

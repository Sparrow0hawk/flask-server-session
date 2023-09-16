from flask import Flask, session, redirect, url_for
from flask_session import Session


def create_app() -> Flask:

    app = Flask(__name__)
    app.config.from_mapping(
        SESSION_TYPE="filesystem",
        SESSION_FILE_DIR="cache"
    )
    Session(app)

    @app.route("/")
    def index() -> str:
        if session.get("user"):
            return f"<h1>Hello {session['user']}!</h1>"
        else:
            return "<h1>Hello world!</h1>"

    @app.route("/user/")
    def user():
        session["user"] = "user1"
        return redirect(url_for("index"))

    return app

from flask import Flask


def create_app() -> Flask:

    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        return "<h1>Hello world!</h1>"

    return app

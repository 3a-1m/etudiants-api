from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["TESTING"] = True

    from .routes.routes import register_routes
    register_routes(app)

    return app

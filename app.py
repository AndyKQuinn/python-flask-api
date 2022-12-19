from flask import Flask, jsonify
from flask_cors import CORS
import goodness


def create_app(config=None):
    app = Flask(__name__)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    @app.route("/ping")
    def ping():
        return "Hello, I appear to be working!"

    # My test endpoint
    # Note that <someId> is for URI params
    @app.route("/serve/<id>")
    def serve_up_some_goodness(id):
        return jsonify(goodness.serving_up_some_goodness(id))

    return app

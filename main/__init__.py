""" Module which creates WSGI application. """
# Python libs.
from flask import Flask
from flask_restplus import Api
# Project files.
from .helpers.main_config import CONFIGURATION
from .helpers.logger import Logger


lg = Logger()
api = Api(doc="/doc/", prefix="/api")


def create_app():
    """ Flask app utilization. """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = CONFIGURATION.secret_key

    # Register api.
    api.init_app(app)

    from .rest_api.bidder.routes import NAMESPACE as bid_ns
    from .rest_api.campaign.routes import NAMESPACE as camp_ns

    # Register resources.
    api.add_namespace(bid_ns)
    api.add_namespace(camp_ns)

    return app

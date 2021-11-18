from flask import Flask

# from application.route_parsing import KwargsConverter
from simplecomputingcluster.register import batch_wrap


def init_app():
    app = Flask(__name__, instance_relative_config=False)

    import config
    from simplecomputingcluster.rq import rq

    # Flask configuration
    app.config.from_object(config.FlaskConfig)

    # Linking Redis Queue to Flask
    rq.init_app(app)

    # Defining which functions will be registered on Redis Queue
    # batch_wrap(config.functions_to_register, rq.job)

    # Defining custom parser of url: not needed now.
    # app.url_map.converters["kwargs"] = KwargsConverter

    with app.app_context():
        from .routes import scc_webapi

        # Registering the general "post" route.
        app.register_blueprint(scc_webapi)

        return app

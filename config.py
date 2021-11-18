FLASK_URL = "http://192.168.178.20:8957"

# These functions are registered as Flask-RQ2 jobs.
functions_to_register = [
    "simplecomputingcluster.jobs.long_lasting_job_simulation",
]

class FlaskConfig:
    """Flask app configuration class.

    Flask blueprint is general enough to encompass all registered functions that pass jsonsable objects.

    In future, could handle custom serialization protocols as plugins.
    Load plugins that would be stored somewhere in a DB?
    """
    RQ_REDIS_URL = "redis://localhost:6379/0"

    @classmethod
    def parsed_url(cls):
        url_port_db = cls.RQ_REDIS_URL.split("//")[1]
        url, port_db = url_port_db.split(":")
        port, db = port_db.split("/")
        port = int(port)
        return {"url": url, "port": port, "db": db}

#TODO this should be dynamically read from some toml or yaml instead!
#Add it to bin/wsgi.py
"""General routing system to assure minimal pairing between routes and the underlying code."""
from flask import Blueprint, request, jsonify
from importlib import import_module

from simplecomputingcluster.register import footype2getfoo, footype2resultwrap, get_foo, batch_wrap



scc_webapi = Blueprint("scc_webapi", __name__)


@scc_webapi.route("/")
def home():
    return "alcomer_backend operational!"


@scc_webapi.route("/post/<footype>", methods=["POST"])
def post(footype):
    if request.is_json:
        module_foo_path, args, kwargs = request.get_json()
        foo = footype2getfoo[footype](module_foo_path)
        result = foo(*args, **kwargs)
        print(result)
        result = footype2resultwrap[footype](result)
        return jsonify(result)


@scc_webapi.route("/register_as_rq_job", methods=["POST"])
def register():
    if request.is_json:
        module_foo_paths = request.get_json()
        from simplecomputingcluster.rq import rq
        batch_wrap(module_foo_paths, rq.job)
        return jsonify(module_foo_paths)
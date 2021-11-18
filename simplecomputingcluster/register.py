from importlib import import_module

import functools
import requests


def split_module_and_foo_names(module_foo_path):
    split = module_foo_path.split(".")
    module_name = ".".join(split[:-1])
    foo_name = split[-1]
    return module_name, foo_name


def get_foo(module_foo_path):
    module_name, foo_name = split_module_and_foo_names(module_foo_path)
    module = import_module(module_name)
    return getattr(module, foo_name)


def _register_post_call(module_foo_path, url):
    foo = get_foo(module_foo_path)
    def post_call(*args, **kwargs):
        response = requests.post(
            url=f"{url}/post/post_call", json=[module_foo_path, args, kwargs]
        )
        return response.json()
    foo.post_call = post_call


def register_post_call(module_foo_paths, url):
    if not isinstance(module_foo_paths, list):
        module_foo_paths = [module_foo_paths]
    for module_foo_path in module_foo_paths:
        _register_post_call(module_foo_path, url)


def register_as_jobs(module_foo_paths, url):
    response = requests.post(url=f"{url}/register_as_rq_job", json=module_foo_paths)
    return response.json()


def _register_post_queue(module_foo_path, url):
    foo = get_foo(module_foo_path)
    def post_queue(*args, **kwargs):
        response = requests.post(
            url=f"{url}/post/post_queue", json=[module_foo_path, args, kwargs]
        )
        return response.json()
    foo.post_queue = post_queue


def register_post_queue(module_foo_paths, url):
    if not isinstance(module_foo_paths, list):
        module_foo_paths = [module_foo_paths]
    for module_foo_path in module_foo_paths:
        _register_post_queue(module_foo_path, url)


footype2getfoo = {
    "post_call": get_foo,
    "post_queue": lambda module_foo_path: getattr(get_foo(module_foo_path), "queue"),
}


def make_queue_info_json_friendly(result):
    result_id = result.id
    result = result.to_dict()
    del result["data"]
    result["id"] = result_id
    return result


footype2resultwrap = {
    "post_call": lambda result: result,
    "post_queue": make_queue_info_json_friendly,
}


def wrap(module_foo_path, wrapper):
    module_name, foo_name = split_module_and_foo_names(module_foo_path)
    module = import_module(module_name)
    foo = getattr(module, foo_name)
    setattr(module, foo_name, wrapper(foo))


def batch_wrap(module_foo_paths, wrappers):
    if not isinstance(module_foo_paths, list):
        module_foo_paths = [module_foo_paths]
    if not isinstance(wrappers, list):
        wrappers = [wrappers]
    for module_foo_path in module_foo_paths:
        for wrapper in wrappers:
            wrap(module_foo_path, wrapper)

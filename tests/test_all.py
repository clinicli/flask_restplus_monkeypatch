import copy
import json
import logging
import sys
import unittest

from flask import Flask, Response, url_for
import flask_restplus

from http import HTTPStatus
from werkzeug import exceptions

import flask_restplus_monkeypatch as frm

logging.basicConfig(stream=sys.stdout,format='    %(levelname)s: %(message)s')
logging.getLogger("FRM.unit_tests").setLevel(logging.DEBUG)

# Some global variables:
logger = logging.getLogger("FRM.unit_tests")
name = "test_app"
app = Flask(name)
base_url = "/api"

class MyTestCase(unittest.TestCase):

    # def test_00100_debug(self):
    #     global app, logger, name
    #     app = frm.apply(app,debug=True)

    # def test_00200_example(self):
    #     global app, logger, name
    #     app, *_ = frm.apply(app,example=True)

    def test_00300_fix_error_router(self):
        global app, logger, name
        Api = flask_restplus.Api
        app = frm.apply(
            app,
            fix_error_router={
                "Api": Api,
                "logger": logger,
            }
        )

        func_name = "fix_error_router"
        assert Api.error_router.__name__ == func_name, \
            "Expected '" + func_name + "', instead got '" + \
            str(Api.error_router.__name__) + "'"

    def test_00400_fix_external_specs_endpoint(self):
        global app, logger, name
        Api = flask_restplus.Api
        blueprint_name = "api"
        app = frm.apply(
            app,
            fix_external_specs_endpoint={
                "Api": Api,
                "blueprint_name": blueprint_name,
                "url_prefix": base_url,
            }
        )

        assert (type(Api.specs_url) == property), \
            "Expected func to be of type 'property', instead got '" + \
            str(type(Api.specs_url)) + "'"

        response = app.test_client().get(base_url + "/swagger.json")
        assert response.status_code == 200, \
            "Expected to find swagger.json at " + str(base_url) + "/swagger.json but " + \
            "instead got response: " + str(response)

    def test_00500_serve_swagger_from_custom_path(self):

        # Note Flask and Flask RESTPlus do not have any means
        # for *deleting* routes, so the old route will remain.

        global app, logger, name

        Api = flask_restplus.Api
        blueprint_name = "docs"
        doc_path = "/doc"
        app, api = frm.apply(
            app,
            serve_swagger_from_custom_path={
                "Api": Api,
                "blueprint_name": blueprint_name,
                "doc_path": doc_path,
            }
        )

        list_urls = "\n\n"
        for u in app.url_map.iter_rules():
            list_urls += "    Registered route: " + str(u) + "\n"

        response = app.test_client().get(doc_path + "/swagger.json")
        assert response.status_code == 200, \
            "Expected to " + str(doc_path) + "/swagger.json but " + \
            "instead got response: " + str(response) + \
            list_urls


# Define some routes on the app.
# Using JSONAPI.org recommendations to avoid bike-shedding.

@app.route("/")
def index():
    return Response(
        json.dumps({"data": None}),
        status=HTTPStatus.OK.value,
        mimetype="application/vnd.api+json"
    )

@app.route(base_url)
def api():
    return Response(
        json.dumps({"data": None}),
        status=HTTPStatus.OK.value,
        mimetype="application/vnd.api+json"
    )

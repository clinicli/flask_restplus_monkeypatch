import copy
import json
import logging
import sys
import unittest

from flask import Flask, Response
import flask_restplus

from http import HTTPStatus
from werkzeug import exceptions

import flask_restplus_monkeypatch as frm

logging.basicConfig(stream=sys.stdout,format='%(message)s')
logging.getLogger("FRM.unit_tests").setLevel(logging.DEBUG)

logger = logging.getLogger("FRM.unit_tests")
name = "test_app"
app = Flask(name)

base_url = "/api"

class MyTestCase(unittest.TestCase):

    # def test_00100_debug(self):
    #     frm.apply(app,debug=True)

    # def test_00200_example(self):
    #     frm.apply(app,example=True)

    def test_00300_fix_error_router(self):
        Api = flask_restplus.Api
        frm.apply(app,
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
        Api = flask_restplus.Api
        blueprint_name = "api"
        frm.apply(app,
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

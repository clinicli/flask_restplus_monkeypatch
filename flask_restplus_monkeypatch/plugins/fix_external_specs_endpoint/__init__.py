"""
Ensure the specs endpoint is not treated as an 'external' resource.
"""

# FIXME Split this into two: one for endpoint fix, one for swagger.json URI fix.

from flask import Blueprint, current_app, url_for

def init(app,**kwargs):

    Api = kwargs["Api"]
    blueprint_name = kwargs["blueprint_name"]
    url_prefix = kwargs["url_prefix"]
    app_name = app.name
    if "app_name" in kwargs:
        app_name = kwargs["app_name"]

    @property
    def fix_specs_url(self):
        return url_for(self.endpoint('specs'), _external=False)
    Api.specs_url = fix_specs_url

    blueprint = Blueprint(blueprint_name, app_name, url_prefix=url_prefix)
    Api(blueprint)
    app.register_blueprint(blueprint)

    return app

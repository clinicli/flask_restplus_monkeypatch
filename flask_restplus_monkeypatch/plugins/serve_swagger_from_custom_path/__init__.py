from flask import Blueprint

def init(app,**kwargs):
    Api = kwargs["Api"]

    blueprint_name = kwargs["blueprint_name"]
    doc_path = kwargs["doc_path"]
    app_name = app.name
    if "app_name" in kwargs:
        app_name = kwargs["app_name"]

    def custom_render_doc(self):
        if self._doc_view:
            return self._doc_view()
        elif not self._doc:
            self.abort(404)
        r = render_template("swagger-ui.html", title=self.title, specs_url=self.specs_url)

    blueprint = Blueprint(
        blueprint_name,
        app_name,
        url_prefix=doc_path
    )
    api = Api.render_doc = custom_render_doc
    Api(blueprint, doc=doc_path)
    app.register_blueprint(blueprint)

    return app, api

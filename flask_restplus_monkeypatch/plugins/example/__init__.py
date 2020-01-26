def init(app,**kwargs):
    """
    Use this example code as a template for your plugin.
    Do NOT change the method signature. It MUST take the Flask app as the first
    argument, and MUST return the app. Any other args can be passed in **kwargs.
    """

    # MUST return app either alone, or as the FIRST item returned:
    return app, 1, 2, 3

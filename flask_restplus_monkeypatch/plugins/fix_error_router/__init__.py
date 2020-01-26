"""
Ensure exceptions are picked up, API responses are produced as expected, and
exceptions are written to the log. Logging code taken from flask_restplus error handler:
https://flask-restplus.readthedocs.io/en/stable/_modules/flask_restplus/api.html#Api.handle_error
"""

import logging
import sys
from flask import current_app

def init(app,**kwargs):
    """
    Docs to go here!
    """

    Api = kwargs["Api"]

    logger = None
    if "logger" in kwargs:
        logger = kwargs["logger"]

    # How to completely silence logging.
    # https://gist.github.com/daryltucker/e40c59a267ea75db12b1
    if logger == False:
        app.logger.disabled = True
        logging.getLogger("werkzeug").disabled = True

    def fix_error_router(self, original_handler, e):
        "Hmm!"
        exc_info = sys.exc_info()
        if exc_info[1] is None:
            exc_info = None
        if (exc_info):
            if logger:
                logger.info(str(e))
            else:
                current_app.log_exception(exc_info)
        else:
            if logger:
                logger.info(str(e))
            else:
                current_app.logger.error(str(e))

        return e

    Api.error_router = fix_error_router

    return app

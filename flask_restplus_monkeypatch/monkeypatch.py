import importlib

from . import plugins as _plugins
from . import const
from . import utils

def apply(app,plugins=[],exclude=[],*args,**kwargs):

    kwargs = utils.tidy_kwargs(kwargs)

    if type(plugins) is str:
        plugins = [ plugins ]
    if type(plugins) is not list:
        raise TypeError("Expected str or list for plugins, got " + str(type(plugins)))

    if type(exclude) is str:
        exclude = [ exclude ]
    if type(exclude) is not list:
        raise TypeError("Expected str or list for exclude, got " + str(type(exclude)))

    for p in [
            str(_)
            for _ in _plugins.discovered_plugins
            if _ not in exclude ]:
        if p not in plugins:
            plugins.append(p)

    for p in plugins:
        _kwargs = {}
        if p in kwargs:
            if type(kwargs[p]) is not dict:
                raise TypeError("Expected dict, got " + str(type(kwargs[p])))
            _kwargs = { **kwargs[p] }
            app = importlib.import_module(utils.module_full_name(p)).init(app,**_kwargs)

    return app

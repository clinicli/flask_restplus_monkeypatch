import importlib

from . import plugins as _plugins
from . import const
from . import utils

def apply(app,plugins=[],exclude=[],debug=False,test=False,example=False,*args,**kwargs):

    _debug = _test = _example = False

    if debug:
        kwargs["debug"] = debug if type(debug) is dict else {}
        _debug = True

    if test:
        kwargs["test"] = test if type(test) is dict else {}
        _test = True

    if example:
        kwargs["example"] = example if type(example) is dict else {}
        _example = True

    if type(plugins) is str:
        plugins = [ plugins ]
    if type(plugins) is not list:
        raise TypeError("Expected str or list for plugins, got " + str(type(plugins)))

    if type(exclude) is str:
        exclude = [ exclude ]
    if type(exclude) is not list:
        raise TypeError("Expected str or list for exclude, got " + str(type(exclude)))

    if not _example: exclude.append(const.example)
    if not _debug: exclude.append(const.debug)
    if not _test: exclude.append(const.test)

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

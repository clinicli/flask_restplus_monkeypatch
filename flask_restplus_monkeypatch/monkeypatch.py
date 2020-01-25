import inspect

from . import plugins
from . import const

def apply(app=None,debug=False,test=False):
    d = __package__ + "." + const.plugins_dir + "."
    exclude = [ d + const.example ]
    if not debug: exclude.append(d + const.debug)
    if not test: exclude.append(d + const.test)

    for p in [ _ for _ in plugins.discovered_plugins if _ not in exclude ]:
        print(p)

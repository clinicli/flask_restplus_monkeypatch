import importlib
import pkgutil

def iter_namespace():
    return pkgutil.iter_modules(__path__, __name__ + ".")

discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in iter_namespace()
}

def load(p):
    pass

def load_all():
    pass


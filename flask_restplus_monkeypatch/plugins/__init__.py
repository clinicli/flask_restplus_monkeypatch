import pkgutil

discovered_plugins = [
    name.split(".")[-1:][0]
    for finder, name, ispkg
    in pkgutil.iter_modules(__path__, __name__ + ".")
]

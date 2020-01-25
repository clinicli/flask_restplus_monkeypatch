from . import const

def module_full_name(m):
    return __package__ + "." + const.plugins_dir + "." + str(m)

def module_short_name(m):
    return str(m.split(".")[0])

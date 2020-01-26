from . import const

def module_full_name(m):
    return __package__ + "." + const.plugins_dir + "." + str(m)

def module_short_name(m):
    return str(m.split(".")[0])

def tidy_kwargs(kw):
    def _swap_true_for_empty_dict(x):
        if isinstance(x, bool) and x is True:
            return {}
        return x
    return {k: _swap_true_for_empty_dict(v) for k, v in kw.items() if v is not False}

# Based on http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991

import sys

class _const:
    class ConstError(TypeError): pass
    def __init__(self):

        # DO NOT EDIT THESE
        self.plugins_dir = "plugins"
        self.example = "example"
        self.test = "test"
        self.debug = "debug"

    def __setattr__(self,name,value):
        if name in self.__dict__.keys():
            raise self.ConstError("Const cannot be re-declared: " + str(name))
        self.__dict__[name]=value

sys.modules[__name__]=_const()

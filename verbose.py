import inspect
import os

from importlib import import_module

def verbose(func):
    def inner_function(*args, **kwargs):
        lines = inspect.getsourcelines(func)
        try:
            with open("tmp_verbose_file_02x91923mxmsk19002177xk.py", "w+") as verbose_file:
                for line in enumerate(lines[0][1:]):
                    verbose_file.write(line[1])
                    verbose_file.write("    " + "print("+str(line[0])+")\n")
            imp = import_module("tmp_verbose_file_02x91923mxmsk19002177xk")
            model = getattr(imp, lines[0][1][lines[0][1].find(" ")+1:lines[0][1].find("(")])
            model(*args, **kwargs)
        finally:
            os.remove("tmp_verbose_file_02x91923mxmsk19002177xk.py")
        return func
    return inner_function
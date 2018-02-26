import inspect
import os

from importlib import import_module

def verbose(func):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    file_name = module.__file__
    def inner_function(*args, **kwargs):

        lines = inspect.getsourcelines(func)

        try:
            print(" ______RUNNING FUNCTION WITH VERBOSE______")
            print("|___________IGNORING DOCSTRINGS___________|")
            print("|                                         |")
            with open("tmp_verbose_file_02x91923mxmsk19002177xk.py", "w+") as verbose_file:
                verbose_file.write("from "+ file_name[0:-3] +" import *\n")
                lock = False
                for line in enumerate(lines[0][1:]):
                    if line[1].lstrip()[0:3] == "\"\"\"" and not lock:
                        lock = True
                    elif line[1].lstrip()[0:3] == "\"\"\"" and lock:
                        lock = False
                    elif not lock:
                        indentation = (len(line[1]) - len(line[1].lstrip())) * ' '
                        verbose_file.write(indentation)
                        verbose_file.write("print(\"" + indentation + "##### LINE OF CODE NO: " + str(line[0]) + " #####" + "\")\n")
                        verbose_file.write(indentation)
                        verbose_file.write("print(\"\"\"" + str(line[1]) + "\"\"\")\n")
                        verbose_file.write(indentation)
                        verbose_file.write("print(\"" + "OUTPUTS:" + "\")\n")
                        verbose_file.write(line[1])
            imp = import_module("tmp_verbose_file_02x91923mxmsk19002177xk")
            model = getattr(imp, lines[0][1][lines[0][1].find(" ")+1:lines[0][1].find("(")])
            model(*args, **kwargs)
        finally:
            print("|_________________________________________|")
            print("|______________END OF VERBOSE_____________|")
            os.remove("tmp_verbose_file_02x91923mxmsk19002177xk.py")

        return func
    return inner_function
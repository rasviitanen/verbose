import inspect
import os
import timeit

from time import sleep
from importlib import import_module

def verbose(func):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    file_name = module.__file__
    this_path = os.path.dirname(os.path.abspath(__file__))
    new_path = file_name[len(this_path)+1:-3].replace("/", ".")

    def inner_function(*args, **kwargs):
        start = timeit.default_timer()
        lines = inspect.getsourcelines(func)

        print(" ______RUNNING FUNCTION WITH VERBOSE______")
        print("|___________IGNORING DOCSTRINGS___________|")
        print("|                                         |")
        with open("tmp_02x91923mxmsk19002177xk.py", "w+") as verbose_file:
            if new_path:
                verbose_file.write("from "+ new_path +" import *\n")
            verbose_file.write("import timeit\n")
            verbose_file.write("start = timeit.default_timer()" + "\n")
            lock = False
            n_docstring_lines = 0
            for line in enumerate(lines[0][1:]):
                if not line[1].lstrip():
                    continue
                elif line[1].lstrip()[0:3] == "\"\"\"" and not lock:
                    lock = True
                    n_docstring_lines = line[0]
                elif line[1].lstrip()[0:3] == "\"\"\"" and lock:
                    lock = False
                elif not lock:
                    indentation = (len(line[1]) - len(line[1].lstrip())) * ' '
                    verbose_file.write(indentation)
                    verbose_file.write("print(\"" + "LINE OF CODE: " + str(line[0] - n_docstring_lines) + "\")\n")
                    verbose_file.write(indentation)
                    verbose_file.write("time_now = timeit.default_timer() - start\n")
                    verbose_file.write(indentation)
                    verbose_file.write("print(\"RUNTIME TO HERE:\" + str(time_now) )\n")
                    verbose_file.write(indentation)
                    verbose_file.write("print('>>>' + \"\"\"" + str(line[1]) + "\"\"\")\n")
                    verbose_file.write(line[1])
            verbose_file.close()

        # Run the created function
        imp = import_module("tmp_02x91923mxmsk19002177xk")
        model = getattr(imp, lines[0][1][lines[0][1].find(" ") + 1:lines[0][1].find("(")])
        model(*args, **kwargs)
        print("|_________________________________________|")
        print("|______________END OF VERBOSE_____________|")
        print("TOTAL RUNTIME WAS: ", timeit.default_timer() - start)
        try:
            os.remove("tmp_02x91923mxmsk19002177xk.py")
            print("Removal of temporary file was successfull!")
        finally:
            print("-------------------------------------------")
        return func(*args, **kwargs)
    return inner_function

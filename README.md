# verbose
Decorator for python, to print a number between each line of code and its output.

Snippet:
```
@verbose
def hello_world():
  print("Hello World!")

hello_world()
```
Output:
```
 ______RUNNING FUNCTION WITH VERBOSE______
|___________IGNORING DOCSTRINGS___________|
|                                         |
LINE OF CODE: 0
RUNTIME TO HERE:9.226999964084825e-06
>>>def hello_world():

LINE OF CODE: 1
RUNTIME TO HERE:0.00010656499989636359
>>>    print("Hello world!")

Hello world!
|_________________________________________|
|______________END OF VERBOSE_____________|
TOTAL RUNTIME WAS:  0.0058718120001231
Removal of temporary file was successfull!
-------------------------------------------
```

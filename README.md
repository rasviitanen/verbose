# verbose
Decorator for python, to print a number between each line of code and its output.

Snippet:
```
@verbose
def hello_world():
  """
  This is a docstring.
  """
  print("Hello World!")

hello_world()
```
Output:
```
 ______RUNNING FUNCTION WITH VERBOSE______
|___________IGNORING DOCSTRINGS___________|
|                                         |
##### LINE OF CODE NO: 0 #####
def hello_world(first_word, second_word):

OUTPUTS:
##### LINE OF CODE NO: 4 #####
    print("Hello World!")

OUTPUTS:
Hello World!
|_________________________________________|
|______________END OF VERBOSE_____________|

```

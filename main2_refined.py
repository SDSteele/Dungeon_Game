from time import sleep
import random
import sys # Importing the sys module to access system-specific parameters and functions

original_print = print #this saves the original print function so we can use it later

def custom_print(*args, **kwargs):
    #args is a tuple of positional arguments, and kwargs is a dictionary of keyword arguments
     """
    A custom print function that calls time.sleep() after printing.
    """
    
    
    _original_print(*args, **kwargs) #call the original print function with the provided arguments
    # the _ before original_print is a convention to indicate that this is a private variable or function
    sys.stdout.flush() #flush the output buffer to ensure that the printed text appears immediately
    #sys. is a module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter
    time.sleep(1) #sleep for 0.5 seconds to create a delay before the next print statement

    print = custom_print #reassign the print function to the custom_print function

print("This is a custom print function that adds a delay after each print statement.")

print("You can use it to create a more dynamic output in your program.")

print("Feel free to modify the delay time or the print messages as needed.")
# ImportDemo.py - Importing modules various ways and the "namespace" concept
# Restart the kernel/clear outputs before running this

#%%% Use the dir() function to list all loaded modules and variables
dir()

#%% Import just one component from a model
from os import path
dir() # See what was imported
print (path.join("C:\\temp","myFile.txt"))

#%% Import a module, giving it a name you choose
import numpy as np
print(dir(np))

#%% Import all subcomponents of a module, giving access to them 
#   without needing to preface a function with the module's name
from math import *
print(dir())
print (sqrt(25))

#%% Remove reference to a specific module from your script/session
del path, np
dir(path) # <-- this will now give you an error



# ANOTHER EXAMPLE OF IMPORTING MODULES

# Import just the path component from the os module:
from os import path
print path.join("C:\\temp","data.txt")

# Import a module but as a shorter name
import pandas as pd
dir(pd) # now we can type "win32c" instead of the full module name of "win32com.client"

# Import all subcomponents of a module at the root level:
from math import *
 sqrt(25) # no longer need math.- prefix! 

# Functions can get confused when two modules share the same function name, for ex. both module A and module B use "factorate" function
 from moduleA import *
 from moduleB import *

# Delete objects from the script/session (these can be be modules or variables):
del path, pd

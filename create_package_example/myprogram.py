# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 02:03:25 2018

@author: Tim
"""

# THIS WOULD BE THE MAIN PROGRAM THAT WANT TO RUN.

# below is example of how to import from a module (a single .py script)
from mymodule import my_func   #form the mymodule.py script, import my_func so now can use it here!

my_func()

# below is example of how to import form a package
# these are like the #include statements that use in C++

from Main_package import myMain_script #importing from Main_package
from Main_package.sub_package import my_sub_script  # importing from subpackage which is inside of Main_package

myMain_script.report_main()  

my_sub_script.sub_report()  #call the  functions from the modules using dot notation
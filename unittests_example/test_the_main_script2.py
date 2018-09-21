# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:56:11 2018

@author: Tim

THIS SCRIPT defines the test functions to test our main_script.py using unit tests
"""

# when writing test functions, want to 1st test the more simple things
# and then test the more complex things

import unittest
import main_script2      #import all the files which want to test (don't need the .py extension)

class TestCap(unittest.TestCase): 
#note: we inherit the class from the package
# unittest called TestCase
    
    # NOTE: we don't need an __init__ method (constructor) here, b/c we don't
    # need to assign any attributes to the class objects upon creation of an object.
    
    def test_one_word(self):
        # what will test with
        text = 'python'
        
        # call the function from main script the want to test
        result =  main_script2.cap_text(text) #use the cap_text function from main_script module
        
        # assert--> meaning state that the result should be equal to Python
        self.assertEqual(result, 'Python')  
        
    def test_multiple_words(self):
        text = 'monty python'
        result = main_script2.cap_text(text)
        self.assertEqual(result,'Monty Python')
        
# if are running this test function directly, then call the main() function from
# unittest package to run the unittest
# WE WANT TO USE THIS IF b/c we will be including this unit test script in our package, and 
# but we don't always  want to run the unit tests. So only when running directly this script,
# will the unit testing occur.
if __name__=='__main__':
    unittest.main()        
    
        
# run this test by using in directory where this script is, from command line: python [name of this test fiel]
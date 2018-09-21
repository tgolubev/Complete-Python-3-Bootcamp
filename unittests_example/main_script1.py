# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:51:51 2018

@author: Tim

This is the main script which will be tested.
"""

def cap_text(text):
    '''
    Input a string
    Output the capitalized string
    '''
    
    return text.capitalize()  #capitalizes 1st letter of every string

    # note: capitalize() does NOT capitalize the 1st letter of every word
    # in the string, so when do the unit test, it will fail, so can see how a 
    # failed unittest looks like.
    
    # to run the unit test, just run the test script, so:
    #python test_the_main_script.py
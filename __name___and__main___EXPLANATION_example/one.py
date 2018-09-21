# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 02:50:20 2018

@author: Tim
"""

def func():
    print("func() in one.py")
    
print("top level in one.py")  #meaning indentation level of 0

if __name__ == '__main__':
    print('one.py is being run directly!')
else:
    print('one.py  has been imported (as a module, from another .py script!')
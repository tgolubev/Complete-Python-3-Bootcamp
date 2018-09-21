# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 02:50:19 2018

@author: Tim
"""

import one

print("top level in two.py")

one.func()

if __name__ == '__main__':
    print('two.py is being run directly!')
else:
    print('two.py  has been imported (as a module, from another .py script!')
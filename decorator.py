# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 22:07:55 2021

@author: Furcas
"""

def disallow_negative(func):
    def inner(*args):
        for arg in args:
            if arg < 0:
                return 0
            print("shavaps!")            
        return  func(*args) 
    
    return inner

@disallow_negative
def foo(x, y):
    return x**y




print(foo(2,8))





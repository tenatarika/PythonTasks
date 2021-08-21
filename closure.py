# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:23:21 2021

@author: Furcas
"""

def example(x,y):
    a = x+y
    b = x*y
    c = a*b
    print(f"a-{a}, b-{b}, c-{c}")
    return c



def next_exaple(x, y):
    a = x+y
    b = x*y
    c = b*a
    print(f"a-{a}, b-{b}, c-{c}")
    def get_value_of_c():
        print(f"return c: {c}")
        return c 
    return get_value_of_c


def private_variable():
    
    value = None 
    
    def set(new_value):
        nonlocal value
        
        value = new_value
        
    def get():
        return value
    return set, get
    
    
a_set, a_get = private_variable()
b_set, b_get = private_variable()

print("обрати внимание на названия функций")
print(a_get, a_set)
print("/////////////////////////////")
print(b_get, b_set)

a_set(10)
print(f"a={a_get()} b ={b_get()}")
b_set(4)
print(f"a={a_get()} b={b_get()}")










    
    
        
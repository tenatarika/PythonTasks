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

# еще пример
def outer(func):
    print(f"Декарируем {func}")
    
    def inner(*args, **kwargs):
        print(f"на вход идет (*{args}, **{kwargs})")
        value = func(*args, **kwargs)
        print(f"выход функции {value}")
        return value
    
    return inner 

@outer
def add_five(num):
    return num+5


print(add_five(5))

# как добавить аргумент 

def add_int_to_all_args(offser):
    def dec(func):
        def inner(*args):
            args = [arg + offser for arg in args]
            
            return func(*args)
        
        return inner
        
    return dec

@add_int_to_all_args(10)
def moo(x, y):
    return x+y

print(moo(1,1))

def innerrr(args, offser):
    args = [arg + offser for arg in args]
    
    return args

print(innerrr([1,1,1,1], 3))

#декоратор на основе класса 

class add_int_to_all_args_by_class:
    def __init__(self, ofset):
        self.ofset = ofset
        
    def __call__(self, func):
        def inner(*args):
            args = [self.ofset + arg for arg in args]
            return func(*args)
        return inner

@add_int_to_all_args_by_class(3)   
def hoo(x,y):
    return x+y+1

print(hoo(1,1))
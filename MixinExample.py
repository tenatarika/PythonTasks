# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 03:33:37 2021

@author: Furcas
"""

class Person():
    food = None
    
    def get_food(self):
        if self.food is None:
            raise ValueError("Food should be set")
        print(f"I like {self.food}")
        
        
        
        
class Student(Person):
    
    food = 'Kebab'
    





s = Student()
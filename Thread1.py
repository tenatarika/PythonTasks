# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:46:20 2021

@author: Furcas
"""

from threading import Thread
from time import sleep

class Myclass:
    def __init__(self, text):
        self.text = text
        
    def __call__(self, count, time):
        for k in range(count):
            sleep(time)
            print('[', k+1, '] ', self.text, sep='')

#print("Начали")
#obj = Myclass("Дочерний поток")

#t = Thread(target = obj, kwargs={"time": 2, "count":5})

#t.start()

#Myclass("Главный поток")(3,1.5)

#if t.is_alive():
#    t.join()
    
#print("The end.")


class OverThread(Thread):
    def __init__(self, count, time, text):
        super().__init__()
        
        self.count = count
        self.time = time
        self.text = text
        
    
    def run(self):
        for k in range(self.count):
            sleep(self.time)
            print(f'[{k+1}] ', self.text, sep='')
            
            
A = OverThread(5,2,"Alpha")
B = OverThread(3, 1.5, "Bravo")

A.start()
B.start()

if A.is_alive():
    A.join()
    
if B.is_alive():
    B.join()
    


            
            
            
            
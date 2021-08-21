# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 02:57:46 2021

@author: Furcas
"""

from threading import * 
from time import sleep

def calc(txt, op):
    
    global number
    
    for k in range(3):
        
        mylock.acquire()
        print(txt, ": ресурс заблокирован", sep="")
    
        try:
            print(txt,"прочитано:", number)
            val = number
            sleep(1)
            if op:
                number = val+1
            else:
                number = val-1 
                
            print(f"{txt} записано {number}")
            
            
        finally:
            print(txt, ": ресурс разблокирован", sep='')
            print("-----------------------")
            
            mylock.release()
        sleep(1)


number = 0
mylock = Lock()

A = Thread(target=calc, args=["A", True])
B = Thread(target=calc, args=["B", False])


A.start()
B.start()

A.join()
B.join()





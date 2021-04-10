# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 00:53:48 2021

@author: Furcas
"""

def task1(fileName, numofLines):
    f = open(str(fileName), 'r'   )  
    ans = []
    for i in range(numofLines):
        ans.append(f.readline())
        
    return ans

print(task1('Sutnic.txt', 5))



def task2(fileName, N1, N2):
    with open(str(fileName), 'r') as f:
        return f.read()[N1:N2]

#print(task2("mank.txt", 2, 6))


def task3(fileName):
    f = open(fileName, "r")
    words = f.read();
    
    
     
    
    return max(words.split())


#print(task3("mank.txt"))

def task4(fileName, listOfWords):
    with open(str(fileName), 'w') as f:
        for word in listOfWords:
            
            f.writelines(word+'\n')
            
    
    return None


#print(task4("Sutnic.txt", ['Aliens', 'BladeRunner', 'Pi', '1=1', 'oldboy']))

def task5(fileName, sWord):
    
    with open(str(fileName), 'r') as f:
        words = f.read().split()
    
    for word in words:
        if word == sWord:
            return True
        else:
            continue

    return False

#print(task5('Sutnic.txt', 'Pi'))


def task6(fileName):
    
    with open(str(fileName), 'r') as f:
        words = f.read().split()
    
    strwords = "".join(words)
    
    namesDict = {}
    for word in words:
        
        
        namesDict.update({str(word):strwords.count(word)})
        
    
    return namesDict
    
#print(task6('Sutnic.txt'))
   

def task7(s):
    s = s.lower()
    if s.replace(' ','')[::-1] == s.replace(' ',''):
        return True
    else:
        return False
    
#print(task7("Able was I ere I saw Elba"))

def task8(s):
    u = 0
    l = 0
    for item in s:        
        if item.islower():
            l +=1
        else:
            u +=1        
    return {'upper': u, 'lower': l}

#print(task8("KokdsdJJJfsdadFFFF"))
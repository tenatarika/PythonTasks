# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 00:53:48 2021

@author: Furcas
"""

def task1(fileName, numofLines):
    '''
    

    Parameters
    ----------
    fileName : TYPE
        DESCRIPTION.
    numofLines : TYPE
        DESCRIPTION.

    Returns
    -------
    ans : TYPE
        DESCRIPTION.

    '''
    f = open(str(fileName), 'r'   )  
    ans = []
    for i in range(numofLines):
        ans.append(f.readline())
        
    return ans

#print(task1('Sutnic.txt', 5))



def task2(fileName, N1, N2):
    '''
    

    Parameters
    ----------
    fileName : TYPE
        DESCRIPTION.
    N1 : TYPE
        DESCRIPTION.
    N2 : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    with open(str(fileName), 'r') as f:
        return f.read()[N1:N2]

#print(task2("mank.txt", 2, 6))


def task3(fileName):
    '''
    

    Parameters
    ----------
    fileName : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    f = open(fileName, "r")
    words = f.read().split();
    
    d_ans = {len(i):i for i in words}
    
    
    
    return d_ans[max(d_ans)]
    


#(task3("Sutnic.txt"))

def task4(fileName, listOfWords):
    '''
    

    Parameters
    ----------
    fileName : TYPE
        DESCRIPTION.
    listOfWords : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    with open(str(fileName), 'w') as f:
        for word in listOfWords:
            
            f.writelines(word+'\n')
            
    
    return None


#print(task4("Sutnic.txt", ['Aliens', 'BladeRunner', 'Pi', '1=1', 'oldboy']))

def task5(fileName, sWord):
    '''
    

    Parameters
    ----------
    fileName : TYPE
        DESCRIPTION.
    sWord : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    '''
    
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
    '''
    

    Parameters
    ----------
    fileName : TYPE
        DESCRIPTION.

    Returns
    -------
    namesDict : TYPE
        DESCRIPTION.

    '''
    
    with open(str(fileName), 'r') as f:
        words = f.read().split()
    
    strwords = "".join(words)
    
    namesDict = {}
    for word in words:
        
        
        namesDict.update({str(word):strwords.count(word)})
        
    
    return namesDict
    
#print(task6('Sutnic.txt'))
   

def task7(s):
    '''
    

    Parameters
    ----------
    s : str
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    '''
    s = s.lower()
    if s.replace(' ','')[::-1] == s.replace(' ',''):
        return True
    else:
        return False
    
#print(task7("Able was I ere I saw Elba"))

def task8(s):
    '''
    

    Parameters
    ----------
    s : str
        DESCRIPTION.

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    u = 0
    l = 0
    for item in s:        
        if item.islower():
            l +=1
        else:
            u +=1        
    return {'upper': u, 'lower': l}

#print(task8("KokdsdJJJfsdadFFFF"))
import numpy as np

from numpy import array

def choice():
    print('Do you wish to 1)encrypt-(e) or 2)decrypt-(d) the message?')
    service=input()
    if service=='e':
        return True
    elif service=='d':
        return False
    else :
        choice()

def getMsg():
    print('Enter your message:')
    return input()

def getKey():
    print('Enter the key:')
    return int(input(),10)


def getTranslatedMsg(edchoice,msg,key):
    translated=''
    i=0
    j=0
    k=0
    
    
    arr=list(msg)
    
    
    
    
    if edchoice==True:
        
        moderr=len(arr)%key
        if(moderr!=0):
             for k in range(0,key-moderr):
                 arr.append('.')
            
        col=int(len(arr)/key)
        fin_arr=array(arr).reshape((col,key))
        print(fin_arr)
        
        for i in range(0,key):
            for j in range(0,col):
                translated+=fin_arr[j][i]
    
        print(translated)  
        
       
    if edchoice==False:
        
        moderr=len(arr)%key
        if(moderr!=0):
             for k in range(0,key-moderr):
                 arr.append('.')
            
        col=int(len(arr)/key)
        fin_arr=array(arr).reshape((key,col))
        print(fin_arr)
        
        for i in range(0,col):
            for j in range(0,key):
                translated+=fin_arr[j][i]
    
        print(translated)    
           
    
   
                       
        
        
            
            
edchoice= choice()
msg=getMsg()
key=getKey()

getTranslatedMsg(edchoice,msg,key)           
    


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

def getTranslatedMsg(edchoice,msg):
    translated=''
    i=0
    j=0
    
    arr=list(msg)
    print (len(arr))
    numarr=[]
    for i in range(0,len(arr)):
                
        numarr.append(ord(arr[i]))
    print (numarr)    
    if edchoice==True:
                       
        
        for j in range(1,26):
            
            for i in range(0,len(numarr)):
                
                if ((chr(numarr[i])=='z') or (chr(numarr[i])=='Z')):
                    numarr[i]=96
                            
                numarr[i]+=j
                translated+=chr(numarr[i])
                
                if ((chr(numarr[i])=='z') or (chr(numarr[i])=='Z')):
                    numarr[i]=96
                    
                numarr[i]-=j
                i+=1
            print (translated)
            translated=''
            j+=1
            
    if edchoice==False:
                       
        
        for j in range(1,26):
            
            for i in range(0,len(numarr)):
                
                if ((chr(numarr[i])=='a') or (chr(numarr[i])=='A')):
                    numarr[i]=123
                            
                numarr[i]-=j
                translated+=chr(numarr[i])
                
                if ((chr(numarr[i])=='a') or (chr(numarr[i])=='A')):
                    numarr[i]=123
                    
                numarr[i]+=j
                i+=1
            print (translated)
            translated=''
            j+=1 
    
            
            
edchoice= choice()
msg=getMsg()

getTranslatedMsg(edchoice,msg)           
    
    
    
        
        
        
        
        
    
        
    
    

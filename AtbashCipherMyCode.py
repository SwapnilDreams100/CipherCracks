

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
    
    cm=          [['a','z'],   
                  ['b','y'],
                  ['c','x'],
                  ['d','w'],
                  ['e','v'],
                  ['f','u'],
                  ['g','t'],
                  ['h','s'],
                  ['i','r'],
                  ['j','q'],
                  ['k','p'],
                  ['l','o'],
                  ['m','n']]
                  
    
    
    if edchoice==True:
        for i in range(0,len(arr)):
            for j in range(0, len(cm)):
                if(arr[i]==cm[j][0]):
                    arr[i]=cm[j][1]
                    translated+=arr[i]
                    break

                elif(arr[i]==cm[j][1]):
                    arr[i]=cm[j][0]
                    translated+=arr[i]
                    break

                
        print(translated)                      
        
    if edchoice==False:
        for i in range(0,len(arr)):
            for j in range(0, len(cm)):
                if(arr[i]==cm[j][0]):
                    arr[i]=cm[j][1]
                    translated+=arr[i]
                    break

                elif(arr[i]==cm[j][1]):
                    arr[i]=cm[j][0]
                    translated+=arr[i]
                    break

                
        print(translated)                      
        
        
        
            
            
edchoice= choice()
msg=getMsg()

getTranslatedMsg(edchoice,msg)           
    
    
    
        
        
        
        
        
    
        
    
    

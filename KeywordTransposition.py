from numpy import array


def getMsg():
    print('Enter your message:')
    return input()

def getKey():
    print('Enter the key:')
    return input()


def getTranslatedMsg(msg,key):
    i=0
    j=0
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    spaces=[]
    
   
    #Create list of msg letters
    arr3=list(msg)
    
    #Create list of alphabets
    arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    #Create list of key characters
    arr2=list(key)
    
    print(arr2)
    
    #Create array to store location of spaces
    for i in range(0,len(arr3)):
      if arr3[i]==' ':
        spaces.append(i)
    
    #Remove spaces
    arr3[:]=[i for i in arr3 if i != ' ']
    
    
    #Delete duplicates from message
    for i in range(0,len(arr2)): 
      for j in range(0,len(arr)-1):
        if(arr2[i]==arr[j]):
          arr.pop(j)

    
    #Delete duplicates from the key
    from collections import OrderedDict
    arr2=list(OrderedDict.fromkeys(arr2))
    print(arr2)
    
    #Create a combined list 
    arr=arr2+arr
    print(arr)
    
    #Sorted key list
    alpharr=sorted(arr2)
    print (alpharr)
    
  
    # creation of final matrix of both key and alphabets    
    moderr=len(arr)%len(arr2)
    if(moderr!=0):
         for k in range(0,len(arr2)-moderr):
             arr.append('')
        
    col=int(len(arr)/len(arr2))
    fin_arr=array(arr).reshape((col,len(arr2)))
    print(fin_arr)
    
    #printing out new aphabet
    trans=''
    for i in range(0,len(arr2)):
      for j in range(0,len(arr2)):
        if(fin_arr[0][j]==alpharr[i]):
          for k in range(0,col):
            trans+=(fin_arr[k][j])
            
    tr=list(trans)
    print(tr)
    
    result=[]
    
    #making matrix of alphabet and new substituted alphabet
    for i in range(0, len(tr)):
      result.append([tr[i],alphabet[i]])
    print(result)
    
    fin=[]
    print(arr3)
    for i in range(0,len(arr3)):
            for j in range(0, 26):
                if(arr3[i]==result[j][0]):
                    fin.append(result[j][1])
                    break
                    
                    
                    
    print(fin)
    
    for i in range(0,len(spaces)):
      fin.insert(spaces[i], ' ')
    str1 = ''.join(fin) 
    print(str1)   
    
msg1=getMsg()
key1=getKey()
getTranslatedMsg(msg1,key1)
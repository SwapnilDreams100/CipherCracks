
plain_text=input("Gimme A String")
cipher_text=''
recieved_text=''
     

def encrypt():
    
     cipher_text=plain_text[::-1]
     return cipher_text

print(encrypt())
     
def decrypt():
    
     received_text=cipher_text[::-1]
     return received_text

print(decrypt())
     
     
     
    


    
     




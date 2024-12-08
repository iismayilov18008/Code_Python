import random

def passwdGenerator():
    UpperCounter=0
    LowerCounter=0
    digitCounter=0
    symbolCounter=0
    password=""
    for i in range(8):
        a=random.choice(range(33, 126))
        password+=chr(a)
        if (a>=65 and a<=90):
            UpperCounter+=1
        if (a>=48 and a<=57):
            digitCounter+=1
        if((a>=33 and a<=64) or (a>=91 and a<=96) or (a>=123 and a<=126)):
            symbolCounter+=1
        if(a>=97 and a<=122):
            LowerCounter+=1
    if (UpperCounter>=1 and digitCounter>=1 and LowerCounter >=1 and symbolCounter>=1):
        print(password)
        exit()
    else:
        passwdGenerator()   
passwdGenerator()     
            
            



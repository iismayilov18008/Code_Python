import random

def passwdGenerator():
    a1=chr(random.choice(range(65, 90)))
    a2=chr(random.choice(range(48, 57)))
    a3=chr(random.choice(range(33, 47)))
    a4=chr(random.choice(range(97, 122)))
    p = [a1, a2, a3, a4]
    for i in range(4):
        p.append(chr(random.choice(range(33, 126))))
    random.shuffle(p)
    return "".join(p)        

print(passwdGenerator()    ) 
            
            



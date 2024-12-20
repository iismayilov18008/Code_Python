import random
a=random.randint(1, 100) # 90
# print(a)
min=1
max=100
while True:
    try:
        b=int(input("Guess the number: "))  # 10 
        if(b<min or  b>max):
            print("Your are out of range")
            continue
        elif(a>b):
            min=b
            
            print(f"too low search between {min} and {max}")
            
        elif(a<b):
            max=b
            print(f"too high search between {min} and {max}")
        if(a==b):
            print(f"{b} is correct ")
            break    
    except Exception as e:
         print(e)
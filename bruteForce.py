import hashlib
hash1=input("enter the hash: ") # 482c811da5d5b4bc6d497ffa98491e38
f=open("words.txt", "r")
for i in f:
    i=i.strip()
    hashing=hashlib.md5(i.encode()).hexdigest()
    
    
    print(hashing)
    if(hashing==hash1):
        print(f"the word is: {i}")
        exit()
print("tapilmadi.")
     
        
        
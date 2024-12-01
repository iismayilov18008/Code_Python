a=input("1ci: ")
b=input("2ci: ")
try:
    c=int(a)//int(b)
    print(c)
except ZeroDivisionError :
    print("sifira bolunmur")    
except ValueError :
    print("deyer duzgun deil")
    
    
    
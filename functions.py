# def func(a, b, c):
#     print(a, b)
# func("akif", "emiray", "vinyl")


def encoding(a, b="utf-8"):
    if(b.lower()=="utf-8"):
        return [i.encode("utf-8") for i in a]
    elif(b.lower()=="hex"):
        return [i.encode().hex() for i in a]
    
    


a=input("1.: ")
b=input("2.: ")

if (not b):
    print(encoding(a,))
else:
    print(encoding(a, b))

    
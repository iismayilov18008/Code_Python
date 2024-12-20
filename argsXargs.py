# *args, **kwargs --> funksiyaya verilen argumentlerin sayi belli olmuyanda istifade olunur

# def func(*args):
#     print(args, type(args))
# func(1, 2) # (1, 2) <class 'tuple'>

########## # instead of *args  we can write everything like *qaraBala, at least there is a star in front of it
# def summing(*args):
#     res=0
#     for num in args:
#         res+=int(num)
#     return res


# nums=[]
# while True :
#     num=input("enter the number: ")
#     if not num:
#         print(summing(*nums))
#         break
#     else:
#         nums.append(int(num))
###################


def salam(*nicat, **nuraya):
    if("operation" in nuraya and nuraya["operation"] == "sum" ):
        print("xelloWorld")
    print(type(nuraya))
salam()    # <class 'dict'>
salam(1, operation="+", action="print" )


# meselen
def reg(*args, **kwargs):
    profile={}
    for keys, values in kwargs.items():
        profile[keys]=values
        print("user registered", profile)
    
# assert --> meselenn "assert a.isnumeric()" bu o demekdir ki, a mutleq reqem olmalidir yoxsa funksiya diyanacaq.

def cem(*args):
    res=0
    for i in args:
        assert i.isnumeric()
        res+=i
    print(f"cemi: {res}")
    






    
        





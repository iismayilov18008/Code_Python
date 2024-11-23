# var="string"

# print(var.index("i"))
# print(type(var))
# print(var.split("r"))

# # we can also write like this
# var1="""salam 
# necesen"""
# print(var1) # it creates two lines. like \n

# var2="""salam necesen 
#sagol yaxsiyam"""

# print(*var2.split()) # salam necesen sagol yaxsiyam # passes the elements individually from the print
# print(var2.split()) # ['salam', 'necesen', 'sagol', 'yaxsiyam'] #passes the whole list from the print

# ss=var2.split()

# print(ss)

# ss[2]="salamat"

# print(*ss)

# in python arrays and lists are mutuble, but strings are immutable

 #strips, lstrip, rstrip, strip bosluqlari silmek ucundur, soldan sagdan yadaki her terefden.

# variable="111char111" ################################
# print(variable.strip("1")) # char
# print(variable.strip("1"), "salam") # char salam --> eger orda +"salam" olsaydi aradaki bosluqda gedeceydi

# lower upper #############################
# salam="salam qaqa Necesen"
# print(salam.upper())
# print(salam.lower())

#find rfind index #######################
# index --> finds the index of smth
# new="salam anecesen alma armud"   # eger axtardigin sey indexde yxdusa meselen asnecesen onda error verecey amma find da yox.
# print(new.index("a")) 
# rfind da sagdan axtarir. find ozu default olaraq soldan baslayir.

#   Task count the word int the string.



# with list ########################3
# counter = 0
# variable = "salam necesen world helloworld world salam world newworld world world world"
# words = variable.split()

# for i in range(len(words)):
#     if words[i] == "world":  
#         words[i] = "mars"
        
# variable = " ".join(words)  # Reconstruct the string
# print(variable)

#with string #############################
# counter = 0
# noncounter = 0
# variable = "salam necesen world helloworld world salam world newworld world world world"

# for i in range(len(variable)):
#     if variable[i:i+5] == "world":  
        
#         if i == len(variable) - 5:
#             counter += 1
#             variable = variable[:i] + "mars" + variable[i+5:]
#             break
        
#         if (i == 0 or variable[i-1] == " ") and (i + 5 == len(variable) or variable[i+5] == " "):
#             counter += 1
#             variable = variable[:i] + "mars" + variable[i+5:]
# # elif i + 6 < len(variable) and (variable[i+6] != " " or variable[i-1] != " "):
# #     counter += 1
# #     noncounter +=1
# print(variable)
# print(f"the number of all of the world s even within the one word: {counter}")
# #print(f"the number of  world s seperately: {counter-noncounter}")

# # inside ##############################
# print("", '') # bele ferqi yoxdur, lakin eger string in icinde dirnaqlar varsa onda problem yaranacaq
# print("kitablar\"\'\'")   # \ escape etmek ucundur, yeni meselen \' veya \" beledise onda hemin seyi escape edecek yeni print edecek.
# tek dirnagin icinde cut i cut dirnagin icinde ise teki escape elemeye ehtiyac yoxdur.


# dir  ##################################
# dir ederek her hansi bir variable hansi methodlari ve funksiyalari icra edir onu gore bilerik.
# var="salam qaqa necesen"
# print(dir(var)) # ['__add__', '__class__', '__dir__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']






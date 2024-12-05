# list=[]
# list.append(0)
# print(list)
# list.append(2)
# print(list)
# list.append(1)
# print(list)
# # # append add element to the end
# list.pop()
# # list.append(1)
# print(list)
# # # pop removes elements from the end
# list.append("salam qaqa")
# print(list)
# list.append(1)
# print(list)
# list.remove(1)
# print(list)
# list.pop(1)
# # # pop(indexOfElementInList)
# print(list)

# list1=[1, 2, 5]
# list2=[6, 7, 8]
# list1 += list2
# print(list1) # [1, 2, 5, 6, 7, 8]

# list3=list1.copy() # creates the copy of the list independent from the list3
# list4=list1 # list4 is dependent on list1 like hardlink

# list5=[1, 11, 22, 112, 223232, 42424]
# list5.insert(1, "salam qaqa") # adds the element between 0 and 1 st element
# print(list5)

# array sorting
# list11=[1, 3, 2, 5, 2, 4, 6, 8, 3, 6, 6, 67, 89, 23, 4, 3]
# print(sorted(list11)) # list11.sort() will not work inside of a print
# list11.sort()
# print(list11) # [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6, 8, 23, 67, 89]
# list11.sort(reverse=True)
# print(list11) # [89, 67, 23, 8, 6, 6, 6, 5, 4, 4, 3, 3, 3, 2, 2, 1]
# listnew=sorted(list11, reverse=True)
# print(listnew) # [89, 67, 23, 8, 6, 6, 6, 5, 4, 4, 3, 3, 3, 2, 2, 1]
# print(reversed(listnew))
# lissst=[3, 2, 4, 6, 3, 5, 6, 66, 2, 4, 3]

# print(list(reversed(lissst))) # [3, 4, 2, 66, 6, 5, 3, 6, 4, 2, 3]

# # but the listnew.reversed() works like sort and changes the array copletely
# here sort works without any variable assignment

# del --
# we can use del to delete any object like class,  array, list and so on. 
# del listnew

# how to assign values to list, we have 2 methods:
# list=[]
# for i in range(10):
#     list.append(i)
# print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # second way 
# list1=[chr(i) for i in range(61, 70)]
# print(list1) # ['=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E'] 

# str
# soz="Salam"
# print(list(soz)) # ['S', 'a', 'l', 'a', 'm']
# print([i.upper() for i in list(soz)]) # ['S', 'A', 'L', 'A', 'M']
# for a aid bele ferqlii cur assign lerin hamini bu tezde [] morterizeler daxilinde yazilir.

# list=["a", "l", "m", "a"]
# print("".join(list)) # alma

# tuple --> immutable
# tuple1=(1, 3, 6, 2, 4)
# print(tuple1, type(tuple1), dir(tuple1)) # <class 'tuple'> and so on
# tuple2=(3, 6, 1, 2, 33, 3)
# print(tuple1+tuple2) #(1, 3, 6, 2, 4, 3, 6, 1, 2, 33, 3)

# # dict
# dict={"key1": "salamQaqaNecsen", 2: "aleykume"}
# print(dict)
# for keys, values in dict.items():
#     print(f"{keys} --> {values}")
#     #key1 --> salamQaqaNecsen
#     #2 --> aleykume
# dict["key2"]="salamlarOlsunSizeCenab"
# # dict.pop("key1") # to delete the item
# deleted = dict.pop("key1")
# print(deleted) # we can even print the deleted item

# update, we have 2 methods, they both do the same work

# phone = {"brand": "Apple", "color": "Red"}
# phone.update({"color": "Blue", "price": 999})
# print(phone)
# Output: {'brand': 'Apple', 'color': 'Blue', 'price': 999}


# phone["color"] = "Blue"
# phone["price"] = 999

# set --> search for "set"  (mutable, no duplicates, unordered)
set={1, 2, 3}
print(set, type(set)) # u can not change the variable in set like set[0]=6
# but u can add or remove the value using set.add() and set.remove()












    
















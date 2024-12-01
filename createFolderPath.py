import os
a=input("enter existing path: ")
b=a
if os.path.exists(a):
    if os.path.isfile(a):
        print("filedir.")
    elif os.path.isdir:
        print("folderdir.")
else:
    os.makedirs(b)
    print("yaradildi.")


    
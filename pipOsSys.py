# meselen bizde file1.py fayli var icerisinde bir den cox funksiya var ve hemin fayldan her hanssa bir funksiyani import elemey isteyirik
# from file1 import summung --> burada biz file1.py dan biz summun i import eledik.

# her hansisa bir fayli import etdikde onun icinde ne varsa onuda import edib ise salacaqdir, meselen print("salam") varsa daxilinde import edilen faylin, onuda print edecek
# meselen eger her seyi import etmek isteyirikse onda biz orada:  from file1 import * yaza bilerik. yadaki sadece import utils de yaza bilerik
 
# pip bir liblary collection dir ve onun icinde tonlarla liblary var ve biz oradan hansinisa yuklemek isteyirikse onda biz:
# pip install requests --> burada biz pip den requests liiblary ni yukledik.


# sys
import sys
sys.exit() # exit code u gosterir ve daxiline deyerlerde vere bilerik meselen -1, 0, 1 ve saiir kimi


print(sys.path) # a list of directories that the interpreter will search in for the required module.

print(sys.maxsize()) # pythondaki en boyuk ededi print edir

print(sys.getrecursionlimit()) # recursiya limitini gosterir, biz burada morterizenin daxiline qoydugumuz deyer ile azaldib ve yaxud artira bilerik.

# os.exit() programi diyandirir
# sys.exit() error code cixardir ve ona gore program diyanir.

#os de file management ucundur: ilk olaraq onu improt etmek lazmdir meselen import os

import os

# file path lerinde \ yerine \\ istifade olunur

print(os.getcwd()) # print current directory

print(os.path.exists()) # var olub olmamasini yoxlayir.

directory=input("enter the directory: ")
file=input("enter the file: ")

print("path: ", os.path.join(directory, file))

# os.path.abspath --> file in absolute path ni qaytarir

# os.path.chdir("..") # cd .. eyni vezifeye sahibdir.

# os.listdir() oldugun yerdeki directory leri list etmek ucundu, icine deyer vererek belli yeri list ede bilerik

# os.makedirs # mkdir -r /salam/xello/privet


# os.rmdir() # silmek ucundur, doluda ola biler 

# os.remove() # used to delete empty directories

# os.path.dirname() # to get the directory name from the specified path




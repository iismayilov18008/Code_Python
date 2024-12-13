f = open("input.txt", "r")
# print(f, type(f))
# print(dir(f))
# f.close()
# File open modes  //fayl oxunanda her fayl bir string sayilir (subheli)
# r --> read
# w --> write
# print(f.readline()) # salam necesen
# print(f.readlines()) # ['alowwww\n', '123\n', 'xello']
# print(f.read()) # hamsini oxuyr alt atla

lines=f.readlines()
for line in lines:
    line=line.strip()
    print(f"[+] {line}")

# f.write() yazmaq ucundur, file i open ederken onun type i ni da deysb write elemeliyk
# f.write("smth\n") yeni line dan yazmaq ucundur file in icine
# f.writelines(["salam\n", "salam2"])

# f.seek(3) --> cursor 3 e dogru gedecey, (0, 1, 2, 3)
# f = open("file.name", "mode") depending on mode u can customuze if u wanna override or append new elements to it

# png to readable form
# ...
# f = open("pic.name", "rb")

# DAY 4 REC 4 BITIR!!!
f.close()





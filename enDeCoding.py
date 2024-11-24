# #UTF-8 ######################
# var="salam"
# varcode=var.encode("utf-8")
# print(varcode) # b'salam'
# print(type(var)) # class string
# print(type(varcode)) # class bytes
# print(varcode[0]) # 115
# int="string".encode("utf-8")
# print(type(int)) # class bytes
# varcodeList=list(varcode)
# print(varcodeList) # [115, 97, 108, 97, 109]
# ss="slamlar"
# bb="salamlar".encode("utf-8")
# cc=ss.encode("utf-8")
# print(ss) # slamlar
# print(list(bb)) # [115, 97, 108, 97, 109, 108, 97, 114]
# print(cc) # b'slamlar'   b--> byte
# print(type(ss))
# print(type(bb))
# print(type(cc)) 
# f=cc.decode("utf-8") #--> list kimi decode elemek olmur sadece string kimi decode ve encode olur elemek.
# print(f) # slamlar
# print(cc[1]) # 108
# print(f[1]) # l

# ASCII #######################

# alma="salam"
# armud=alma.encode("ascii")
# print(armud[0]) # 115
# print(armud) # b'salam'
# list1=list(armud)
# list2=list(alma)
# print(list1) # [115, 97, 108, 97, 109]
# print(*list2) # s a l a m

# chr/ord #####################

# chr --> ascii(unicode) number to a character
# ord --> character to ascii number 
# print(ord("s")) # 115
# print(chr(115)) # s

# print(ord("S")) # 83
# print(chr(115)) # s
# print(ord("s")) # 115
# print(ord("t")) # 116
# print(chr(116)) # t

# Bytes and Bytearray 

# bytes --> immutable
# bytearray --> mutable

# var = bytes("salam".encode())
# print(var[0]) # 115
# # print(list(var)) # [115, 97, 108, 97, 109]
# # var[0] = 116 error 
# var1=bytearray("xello".encode())
# var1[0]=116 
# print(var1) # bytearray(b'tello')
# print(list(var1)) # [116, 101, 108, 108, 111]

# Hex ###############################

# var="string"
# print(var.encode().hex()) # 737472696e67 # from bytes to hex
# hex() den istifade elemey ucun mutelq encode elemy lazdir.
# print(bytes("salm".encode()).hex()) # 73616c6d
# demeli birinci adi string byte a sonrada byte da hex e cevrilir 
# daha sonra ise hex den byte a daha sonra ise onuda decode ile stringe 
# print(bytes.fromhex("73616c6d").decode()) # salm

# String Formatting #######################

#f"salam qaqa {var}"
# yadiviza gelirse "" daxilinde escape \ bu isare idi
# burada ise escape {{ }} her ikisinne qosa qoymaqdir
# var ="Ismayil"
# print(f"menim adim {{{var}}}") # menim adim {Ismayil}
# bunun icerisinde her seyi elemek olar sadece gerey {} daxilinde "" olmasin
# 4 dene A yazmaq ucun {'A'*4}
# int("14", 16) 14 u 16 liq say sisteminden ceviririk
# bu formatting biraz ferqlide yazila biler
# var="my name is {}" # unnamed format
# print(var.format("Ismayil"))
# #named format
# var1="salam {name} necesen"
# print(var1.format(name="Ismayil"))
# :.3f --> yuvarlasdira ucun istifade edilir

# :c unicode | :b binary | :e scientific | :x hex | :%percentage format
# print(f"111 in unicode is {111:c} ")
# print(f"111 in binary is {111:b} ")
# print(f"111 in scientific is  {111:e} ")
# print(f"111 in hex is {111:x} ")
# print(f"111 in percentage is {111:%} ")
# a=f"{111:b}"
# print(a) # 1101111


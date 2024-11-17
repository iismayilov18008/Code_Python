# a=input("enter smth: ")
# b=int(input("enter the encode type: 1= utf-8 , 2 = hex, 3 = binary: "))
# if b==1:
#     c="UTF-8"
# if b==2:
#     c="ascii"
# if b==3:
#     c="hex"
# if (c=="hex"):
#     print(f"encode based of hex: {a.encode(c).hex()} ")
# else: 
#     print(f"encode based on {c}: {a.encode(c)}")
    
a = input("Enter something: ")
b = int(input("Enter the encode type: 1= utf-8, 2= hex, 3= binary: "))

if b == 1:
    c = "utf-8"
elif b == 2:
    c = "hex"
elif b == 3:
    c = "binary"
else:
    print("Invalid encode type.")
    exit()

if c == "hex":
    encoded_hex = a.encode().hex()
    print(f"Encoded as hex: {encoded_hex}")
elif c == "binary":
    encoded_binary = ' '.join(format(ord(i), '08b') for i in a)
    print(f"Encoded as binary: {encoded_binary}")
else:
    encoded_str = a.encode(c)
    print(f"Encoded using {c}: {list(encoded_str)}")  

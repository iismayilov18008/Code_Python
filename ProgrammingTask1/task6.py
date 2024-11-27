# bitti
a=input("enter smth: ")

print(a.encode("utf-8"))
print(a.encode().hex())
binary_encoded = ' '.join(format(byte, '08b') for byte in a.encode("utf-8"))
print(binary_encoded)
# bitti
a=input("Enter the password: ")
boyukHerf="QWERTYUIOPASDFGHJKLZXCVBNM"
kicinHerf="qwertyuiopasdfghjklzxcvbnm"
reqemler="1234567890"
xususiSymb="~`!@#$%^&*()_+-=\{}[]:\";'<>,.?/\|"
counter=len(a)
bcount=0
kcount=0
rcount=0
xcount=0

for i in range(len(a)):
    if(a[i] in boyukHerf):
        bcount+=1
    if(a[i] in kicinHerf):
        kcount+=1
    if(a[i] in reqemler):
        rcount+=1
    if(a[i] in xususiSymb):
        xcount+=1

if (bcount >= 1 and kcount>=1 and rcount >=1 and xcount>=1 and counter>=8):
    print("Password is accepted")
if(counter<8):
    print("Sifre minimum 8 characterden ibaret olmalidir")
if (bcount<1):
    print("Boyuk herf sayi kifayet deyil")
if(kcount<1):
    print("kicik herf sayi kifayet deyil")
if(rcount<1):
    print("reqem sayi kifayet deyil")
if(xcount<1):
    print("Xususi simvol sayi kifayet deyil")



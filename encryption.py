samitler="abcdefghijklmnopqrstuvwxyz"
a=input("enter string: ")
r=int(input("key daxil et: "))
b=[]
for i in range(len(a)):
    d=(samitler.find(a[i])+r)%26
    b.append(samitler[d])
print(*b, sep="")

    


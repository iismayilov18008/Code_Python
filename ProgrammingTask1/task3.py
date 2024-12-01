# bitti
# give the input like: 10.10.10.10./24 
ip1=input("ip1: ")
ip2=input("ip2: ")

i1=ip1.split(".")
i2=ip2.split(".")
if (len(i1) != 5 or len(i2) != 5  ):
    print("IP sehvdir")
    exit()

sub1=int(i1[4].split("/")[1])
sub2=int(i2[4].split("/")[1])

counter=0

for i in range(len(i1)-1):
    if (int(i1[i])>255 or int(i1[i])<0 ):
        counter+=1
for i in range(len(i2)-1):
    if (int(i2[i])>255 or int(i2[i])<0 ):
        counter+=1

if(counter>0):
    print("daxil edilen ip sehvdir")
    exit()

if(ip1==ip2):
    print("IP ler eynidir")
    exit()

if(sub1!=sub2):
    print("elaqe yaradila bilmez cunki subnet ler ferqlidir.")
if(sub1==sub2):
    if(sub1>=24):
        if(i1[0] == i2[0] and i1[1] == i2[1] and i1[2] == i2[2]):
            print("They can communicate")
        else:
            print("They can not communicate")
    if(sub1>=16 and sub1 < 24):
        if(i1[0] == i2[0] and i1[1] == i2[1] ):
            print("They can communicate")
        else:
            print("They can not communicate")
    if(sub1>=8 and sub1 < 16):
        if(i1[0] == i2[0] ):
            print("They can communicate")
        else:
            print("They can not communicate")
    if(sub1 < 8):
        if(i1[0] == i2[0]  ):
            print("They can communicate")
        else:
            print("They can not communicate")





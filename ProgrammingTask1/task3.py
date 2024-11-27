# bitti
ip1=input("ip1: ")
ip2=input("ip2: ")

i1=ip1.split(".")
i2=ip2.split(".")

sub1=int(i1[3].split("/")[1])
sub2=int(i1[3].split("/")[1])

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





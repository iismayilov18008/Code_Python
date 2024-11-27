# yarimciq
ipaddr=input("IpAddr: ")
ip=ipaddr.split(".")
forth=int(ip[3])
# print(ip[4]) # ./24
subnetMask=ip[4].split("/")
subnet=int(subnetMask[1])  # for example 24 as an integer

if subnet>=24 and subnet<=32:
    a=32-subnet
    b=2**a
    if (forth//b==0):
        
        print(f"  network ip: {ip[0]}.{ip[1]}.{ip[2]}.0")
        print(f"broadcast ip: {ip[0]}.{ip[1]}.{ip[2]}.{int((b-1))}")
        
    elif (forth//b>0):
        print(f"network ip: {ip[0]}.{ip[1]}.{ip[2]}.{((forth/b)*b):.0f}")
        print(f"broadcast ip: {ip[0]}.{ip[1]}.{ip[2]}.{(((forth/b)*b)+b-1):.0f}")
        






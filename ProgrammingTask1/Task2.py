# bitti
ipaddr=input("IpAddr: ")
ip=ipaddr.split(".")
if(len(ip)!=5):
    print("IP movcud deil")
    exit()
forth=int(ip[3])
third=int(ip[2])
second=int(ip[1])
first=int(ip[0])
if(first>255 or first<0 or second>255 or second<0 or  third>255 or third<0 or forth>255 or forth<0):
    print("IP addr movcud deyil")
    exit()
    
# print(ip[4]) # ./24
subnetMask=ip[4].split("/")
subnet=int(subnetMask[1])  # for example 24 as an integer
if(subnet>32 or subnet <1):
    print("IP movcud deil")
    exit()


if subnet>=24 and subnet<=32:
    a=32-subnet
    b=2**a
    if (forth//b==0):
        
        print(f"  network ip: {ip[0]}.{ip[1]}.{ip[2]}.0")
        print(f"broadcast ip: {ip[0]}.{ip[1]}.{ip[2]}.{int((b-1))}")
        
    elif (forth//b>0):
        print(f"  network ip: {ip[0]}.{ip[1]}.{ip[2]}.{((forth//b)*b):.0f}")
        print(f"broadcast ip: {ip[0]}.{ip[1]}.{ip[2]}.{(((forth//b)*b)+b-1):.0f}")
    
elif subnet>=16 and subnet<24:
    a=24-subnet
    b=2**a
    if(third//b==0):
        print(f"  network ip: {ip[0]}.{ip[1]}.0.0")
        print(f"broadcast ip: {ip[0]}.{ip[1]}.{int(b-1)}.255")
    elif(third//b>0):
        print(f"  network ip: {ip[0]}.{ip[1]}.{((third//b)*b):.0f}.0")
        print(f"broadcast ip: {ip[0]}.{ip[1]}.{(((third//b)*b)+b-1):.0f}.255")
elif subnet>=8 and subnet<16:
    a=16-subnet
    b=2**a
    if(second//b==0):
        print(f"  network ip: {ip[0]}.0.0.0")
        print(f"broadcast ip: {ip[0]}.{int(b-1)}.255.255")
    elif(second//b>0):
        print(f"  network ip: {ip[0]}.{((second//b)*b):.0f}.0.0")
        print(f"broadcast ip: {ip[0]}.{(((second//b)*b)+b-1):.0f}.255.255")
elif subnet>0 and subnet<8:
    a=8-subnet
    b=2**a
    if(first//b==0):
        print(f"  network ip: {((first//b)*b):.0f}.0.0.0")
        print(f"broadcast ip: {int(b-1)}.255.255.255")
    elif(first//b>0):
        print(f"  network ip: {(((first//b)*b)):.0f}.0.0.0")
        print(f"broadcast ip: {(((first//b)*b)+b-1):.0f}.255.255.255")


# bu taskda, en sonuncu hisse ve bezi elave seyler praktiki cehetden imkansizdir, veya imkansiza yaxindir. lakin men butun oz kodumu, ip calculator larin hesbalama methoduna nezeren eledim.





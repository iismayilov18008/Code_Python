ipaddr=input("IpAddr: ")
ip=ipaddr.split(".")
counter=0

ip1=int(ip[0])
if (ip1>=255 and ip1<=0):
    counter+=1

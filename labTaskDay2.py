ports={22: "SSH", 80: "SSH", 443: "HTTPS", 25: "SMTP" }
while True:
    b=int(input("Enter number: 1 == Query a Port, 2 == Add a Service, 3 == List All Services, 4 == Exit: "))
    if b == 1:        
             a=int(input("Enter a port number: (write exit to leave the option): " ))
             if a in ports:  
                  print(f"port {a} is {ports[a]}")
             else:
                  print(f"There is no port {a} ")
    if b == 2:
            aa=int(input("Enter the new port number: "))
            bb=input("Enter the port name: ")
            if (aa in ports.keys() and bb in ports.values()):
                print("We already have this port.")
            elif (aa not in ports.values() and bb not in ports.values() ):
                print("port is not found")
                ports[aa]=bb
                print(f"{ports[aa]} is added." ) 
            else: 
                print("Provided information is not correct: ")
    
    if b == 3:
        for key, value in ports.items():
            print(f"{key} -> {value}")
    
    if b ==4:
        print("Goodbye!!")
        break
            

                 
    

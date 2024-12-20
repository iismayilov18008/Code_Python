def isPrime(a):
    a=int(a)
    if(a==1):
        print(f"{a} is prime")
        exit()
    for i in range(2, int((a/2)+1)):
        if(a%i==0):
            print(f"{a} is not prime")
            exit()
    print(f"{a} is prime")

a=int(input("Enter the number: "))
isPrime(a)
        
        
d=int(input("enter the number of operations u r going to do: "))
for i in range(d):
    a=float(input())
    b=input()
    c=float(input())
    if(b=="+"):
        print(f"{a} {b} {c}={a+c}")  print(a+" "+b+ " "+c+ "=",a+c)
    if(b=="-"):
        print(f"{a} {b} {c}={a-c}")
    if(b=="*"):
        print(f"{a} {b} {c}={a*c}")
    if(b=="/"):
        print(f"{a} {b} {c}={a/c}")
    if(b=="%"):
        print(f"{a} {b} {c}={a%c}")
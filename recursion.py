a = [0] * 1500

def fibo(n: int) -> int:
    if n == 0:
        a[0] = 0
        return a[0]
    if n == 1:
        a[1] = 1
        return a[1]
    if a[n] != 0:
        return a[n]
    a[n] = fibo(n-1) + fibo(n-2)  
    return a[n] 
counter=0 
while True:
    n=int(input("enter the value: "))
    print(fibo(n)) 
    # counter+=1
    # if counter==10:
    #     break
# print(a)


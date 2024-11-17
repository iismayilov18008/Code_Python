a=int(input("Illik gelirinizi daxil edin: "))
b=0
if (a < 20000):
    b=(a/100)*5
if (a >= 20000 and a<=50000 ):
    b=(a/100)*10
if (a>50000):
    b=(a/100)*15
print("Vergi: ", b, "AZN" )
print("Vergi sornasi gelir: ", a-b, "AZN")
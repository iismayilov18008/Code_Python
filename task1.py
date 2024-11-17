a=int(input("meblegi daxil edin: "))
b=0
if (a > 100):
    b=(a/100)*5
if (a > 300):
    b=(a/100)*10
print("Endirim: ", b, "AZN" )
print("Yekun mebleg: ", a-b, "AZN")


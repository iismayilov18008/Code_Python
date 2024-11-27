# bitti
a=input("operasiyani daxil ele: ")
for i in range(len(a)):
    if(a[i] == "+"):
        num=a.split("+")
        cvb=float(num[0])+float(num[1])
        print(f"{cvb:.3f}")
    if(a[i] == "-"):
        num=a.split("-")
        cvb=float(num[0])-float(num[1])
        print(f"{cvb:.3f}")
    if(a[i] == "*"):
        num=a.split("*")
        cvb=float(num[0])*float(num[1])
        print(f"{cvb:.3f}")
    if(a[i] == "%"):
        num=a.split("%")
        cvb=float(num[0])%float(num[1])
        print(f"{cvb:.3f}")
if("//" in a):
        num=a.split("//")
        cvb=float(num[0])//float(num[1])
        print(f"{cvb:.3f}")
elif("/" in a):
        num=a.split("/")
        cvb=float(num[0])/float(num[1])
        print(f"{cvb:.3f}")

# bu kodda sonradan gordum ki, hec for loop a ehtiyac yox idi.
# burada esas problem / dan sonraki / dedect etmek idi. for loop daxilinde ise butun elementler ucun search ettiyi ucun 44//4 un daxilinde ilk / tapdiginda ondan sonra / oldugunu gorur ve // operationu edir. lakin i, 1 vahid artdiqda ise yene / gelir ve ondan sonra / yoxdur ve o halda ise (444/)/(4) emeliyyatini icr etmeye calisor, ona gorede loop un xaricine alb, orada if elif den istidafe edib ve 1 ci de // case i vererek hell etdim problemi. ancaq biz loop daxilinde a[i] =="/" ve a[i+1] =="/" oldugu halda if case in sonuna i+=1 yazsaydiqda hell olacaqdi, cunki ikinci / u skip edecekdi.


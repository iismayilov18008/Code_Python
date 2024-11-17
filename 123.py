a=int(input("Teyziqi daxil et:"))
b=int(input("Sekeri daxil et:"))
if a>140 & b>120:
    print("Yüksək risk — Həkimə müraciət edin")
if a>130 & a<=140 & b<=120 & b>100:
    print("orta risk - Muntezem yoxlama olunur")
if a<=130 & b<=100:
    print("Asagi Risk - Saglmaliq veziyyetiniz normaldir")
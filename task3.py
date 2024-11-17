a = int(input("Teyziqi daxil et: "))
b = int(input("Sekeri daxil et: "))

if a > 140 and b > 120:
    print("Yüksək risk — Həkimə müraciət edin")
elif 130 < a <= 140 and 100 < b <= 120:
    print("Orta risk - Mütəmadi yoxlama olunur")
elif a <= 130 and b <= 100:
    print("Aşağı risk - Sağlamlıq vəziyyətiniz normaldır")


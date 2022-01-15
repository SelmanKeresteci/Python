def toplama():
    a = int(input("Birinci Sayı: "))
    b = int(input("İkinci Sayı: "))
    print("Sonuç: ", a+b)
def cikarma():
    c = int(input("Birinci Sayı: "))
    d = int(input("İkinci Sayı: "))
    print("Sonuç: ", c-d)
def carpma():
    e = int(input("Birinci Sayı: "))
    f = int(input("İkinci Sayı: "))
    print("Sonuç: ", e*f)
def bölme():
    g = int(input("Birinci Sayı: "))
    h = int(input("İkinci Sayı: "))
    print("Sonuç: ", g/h)
def menu():
    print("**************\n* Toplama- 1 *\n* Çıkarma-2 **\n* Çarpma-3 ***\n* Bölme-4 ****\n**************")
while True:
    menu()
    print("--------------")
    secim = int(input("Seçim: "))
    print("--------------")
    if secim == 1:
        toplama()
    elif secim == 2:
        cikarma()
    elif secim == 3:
        carpma()
    elif secim == 4:
        bölme()
    else:
        break

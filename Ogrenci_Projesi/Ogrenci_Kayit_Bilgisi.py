def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    OgrenciAdi = (liste[0])
    notlar= (liste[1]).split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3)/3

    if ortalama >= 90 and ortalama <=100:
        harf = "AA"
    elif ortalama >=85 and ortalama <=89:
        harf = "BA"
    elif ortalama >=80 and ortalama <=84:
        harf = "BB"
    elif ortalama >=75 and ortalama <=79:
        harf = "CB"
    elif ortalama >=70 and ortalama <=74:
        harf = "CC"
    elif ortalama >=65 and ortalama <=69:
        harf = "DC"
    elif ortalama >=60 and ortalama <=64:
        harf = "DD"
    elif ortalama >=50 and ortalama <=59:
        harf = "FD"
    else:
        harf = "FF"
    return OgrenciAdi + ":" + harf + "\n"



def ortalamaları_oku():
    with open("sinavnotlari.txt","r",encoding="utf-8")as file:
        for satir in file:
            print(not_hesapla(satir))
def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")

    with open("sinavnotlari.txt","a",encoding="utf-8")as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
def notları_kayıt_et():
    with open("sinavnotlari.txt","r",encoding="utf-8")as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n')

    if islem == '1':
        ortalamaları_oku()
    if islem == "2":
        not_gir()
    if islem == "3":
        notları_kayıt_et()
    else:
        pass
    
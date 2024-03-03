def not_hesapla(satir):
    satir = satir[:-1]  # satırlar arasındaki boşlukları siler
    liste = satir.split(":")
    ogrenci_adi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90:
        harf = "AA"
    elif 85 <= ortalama <= 89:
        harf = 'BA'
    elif 80 <= ortalama <= 84:
        harf = 'BB'
    elif 75 <= ortalama <= 79:
        harf = 'CB'
    elif 70 <= ortalama <= 74:
        harf = 'CC'
    elif 65 <= ortalama <= 69:
        harf = 'DC'
    elif 60 <= ortalama <= 64:
        harf = 'DD'
    else:
        harf = "FF"

    return ogrenci_adi + ":" + harf + "\n"

def ortalama_oku():
    try:
        with open("Sinav_Notlari.txt", "r", encoding="utf-8") as dosya:
            for i in dosya:
                print(not_hesapla(i))
    except FileNotFoundError:
        print("Öğrenci Notu Bulunamadı! Lütfen Not Giriniz!")

def not_gir():
    ad = input("Öğrenci Adını Giriniz: ")
    soyad = input("Öğrenci Soyadını Giriniz: ")
    vize1 = int(input("1. Vize Notunu Giriniz: "))
    vize2 = int(input("2. Vize Notunu Giriniz: "))
    final = int(input("Final Notunu Giriniz: "))

    with open("Sinav_Notlari.txt", "a", encoding="utf-8") as dosya:
        dosya.write(ad + " " + soyad + ":" + str(vize1) + "," + str(vize2) + "," + str(final) + "\n")

def notlari_kayit_et():
    sonuclar = []
    with open("Sinav_Notlari.txt", "r", encoding="utf-8") as dosya:
        for x in dosya:
            sonuclar.append(not_hesapla(x))

    with open("Sonuclar.txt", "w", encoding="utf-8") as dosya2:
        for y in sonuclar:
            dosya2.write(y)

while True:
    islem = input("İşlem Seçiniz:\n1-Not Oku\n2-Not Gir\n3-Not Kaydet\n4-Çıkış:\n")
    if islem == "1":
        ortalama_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayit_et()
    else:
        break

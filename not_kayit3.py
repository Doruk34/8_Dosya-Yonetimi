import os
def not_gir():
    ogrenci_adi = input("Öğrenci Adı: ")
    ogrenci_soyadi = input("Öğrenci Soyadı: ")
    vize1 = int(input("1.Vize Notunu Giriniz: "))
    vize2 = int(input("Not 2.Vize Notunu Giriniz: "))
    final = int(input("Final Notunu Giriniz: "))
    
    return {
        "Ad": ogrenci_adi,
        "Soyad": ogrenci_soyadi,
        "Not1": vize1,
        "Not2": vize2,
        "Not3": final
    }
def harf_notu_hesapla(puan):
    if 90 <= puan <= 100:
        return "AA"
    elif 85 <= puan < 90:
        return "BA"
    elif 80 <= puan < 85:
        return "BB"
    elif 75 <= puan < 80:
        return "CB"
    elif 70 <= puan < 75:
        return "CC"
    elif 64 <= puan < 70:
        return "DC"
    elif 60 <= puan < 64:
        return "DD"
    else:
        return "FF"

def notlari_kaydet(ogrenci_notlari):
    harf_notu = harf_notu_hesapla(ogrenci_notlari["Not1"] + ogrenci_notlari["Not2"] + ogrenci_notlari["Not3"])
    ortalama = (ogrenci_notlari["Not1"] + ogrenci_notlari["Not2"] + ogrenci_notlari["Not3"]) / 3

    with open("Sinav_Notlari.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{ogrenci_notlari['Ad']: <15} {ogrenci_notlari['Soyad']: <15} "
                     f"Vize1: {ogrenci_notlari['Not1']: <5} "
                     f"Vize2: {ogrenci_notlari['Not2']: <5} "
                     f"Final: {ogrenci_notlari['Not3']: <5} "
                     f"Harf Notu: {harf_notu: <5} "
                     f"Ortalama: {ortalama:.2f}\n")

def not_oku():
    if os.path.exists("Sinav_Notlari.txt"):
        with open("Sinav_Notlari.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.read()
            print(notlar)    
    else:
        print("Sinav_Notlari.txt dosyası bulunamadı!")

while True:
    print("\n1-Not Gir\n2-Not Hesapla\n3-Not Oku\n4-Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        ogrenci_notlari = not_gir()
        notlari_kaydet(ogrenci_notlari)
        print("Notlar kaydedildi.")
    elif secim == "2":
        if "ogrenci_notlari" in locals():
            harf_notu = harf_notu_hesapla(ogrenci_notlari["Not1"] + ogrenci_notlari["Not2"] + ogrenci_notlari["Not3"])
            print(f"{ogrenci_notlari['Ad']} {ogrenci_notlari['Soyad']}: "
                  f"Harf Notu: {harf_notu} "
                  f"Ortalama: {(ogrenci_notlari['Not1'] + ogrenci_notlari['Not2'] + ogrenci_notlari['Not3']) / 3:.2f}")
        else:
            print("Önce not girmelisiniz.")
    elif secim == "3":
        not_oku()
    elif secim == "4":
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin!")

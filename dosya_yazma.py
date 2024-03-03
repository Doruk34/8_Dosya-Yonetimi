#  Dosya Okuma Yazma open() dosya okuma yazma fonksiyonu

# open("dosya_adi.uzantisi","okuma yazma eklenir",encoding="utf-8")

# Dosya Açma Metotları

# 1) w(write) Methodu:

"""
Yazma methodudur dosyanın içine yazma işlemi yapar.
Eğer belirtelen isimde dosya yok ise yeni dosya açar. 
Eğer belirtilen isimde dosya var ise de içindeki veriyi silip yeniden yazar.
Herhangi bir hata döndürmez.
"""

# open("metin_belgesi.txt","w",encoding="utf-8")
open("C:/Users/....../Desktop/Katar/metin_belgesi.txt","w",encoding="utf-8")
open("C:\\Users\\.....\\Desktop\\Katar\\metin_belgesi.txt","w",encoding="utf-8")
# 2) a(append) Methodu:

"""
Eğer dosyanın içinde veri var ise herhangi bir silme işlemi yapmaksızın verinin sonuna
ekleme yapar. Eğer konuda aynı dosya var ise hata vermez.

"""
# open("metin_belgesi.txt","a",encoding="utf-8")

# 3) x(create) Methodu:
"""
Eğer konuda aynı dosya var ise hata verir.

"""
# open("metin_belgesi.txt","x",encoding="utf-8")

# 4) r(read) Methodu:
"""
Okuma modudur. Eğer belirtilen yolda dosya yok ise hata verir.
"""
# open("metin_belgesi.txt","r",encoding="utf-8")

# 5) r+(read write) Methodu:

"""
Okuma Yazma modudur. Eğer belirtilen yolda dosya yok ise hata verir.
"""
# open("metin_belgesi.txt","r+",encoding="utf-8")

# 5) w+(write read) Methodu:

"""
Yazma Okuma modudur. Eğer belirtilen yolda dosya yok ise hata vermez.
"""
# open("metin_belgesi.txt","w+",encoding="utf-8")

# open("metin_belgesi.pptx","w",encoding="utf-8")

"""W MODU"""

# islem = open("metin_belgesi.txt","w",encoding="utf-8")

# islem.close() # Açık olan dosyayı kapatır.

# islem.write("Python ile W kullanımı")
# print(islem)

"""A MODU"""

# islem = open("metin_belgesi.txt","a",encoding="utf-8")
# islem.write("Python ile a kullanımı ")
# islem.close()

"""X MODU"""
"""Eğer dosya var ise hata verir."""
# islem = open("metin_belgesi.txt","x",encoding="utf-8")
# islem.write("Python ile x kullanımı ")
# islem.close()

try:
    islem = open("metin_belgesi.txt","x",encoding="utf-8")
    islem.write("Python ile x kullanımı ")
except FileExistsError as hata:
    print("Dosya Belirtilen Konumda Mevcut\n",hata)
finally:
    try:
        islem.close()
    except:
        print("İşlem Sonlandı!")

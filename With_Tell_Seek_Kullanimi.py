"""             With            """

# Açılan dosyanın otomatik kapanmasını sağlayan bir fonksiyondur.
# Obje ataması yapılarak kontrol işlemi sağlanır.

# with open("with_kullanimi.txt","w",encoding="utf-8") as dosya:
#     dosya.write("Merhaba")


"""             Seek            """

# with open("with_kullanimi.txt","r",encoding="utf-8") as dosya:
#     print(dosya.read())
#     dosya.seek(5) # İmleç konumunu 5 byte'lık yani 5 karakterden başlatır.


"""             Tell            """

# with open("with_kullanimi.txt","r",encoding="utf-8") as dosya:
#     dosya.seek(0)
#     print(dosya.read())
#     print(dosya.tell())

with open("test.txt","r",encoding="utf-8") as dosya:
    dosya.seek(0)
    print(dosya.read())
    dosya.seek(4)
    print(dosya.tell())
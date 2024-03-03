# yazma = open("okuma.txt","w",encoding="utf-8")
# yazma.write("Merhaba Python")
# yazma.close()
# okuma = open("okuma.txt","r",encoding="utf-8") # veriyi okuma işlemi yapılacak. r yazmasanda olur.

# print(okuma.read())

# Farklı Konumdan Veri Alma

farkli_konum = open("C:\\Users\\.......\\Desktop\\Katar\\Farkli_konum.txt","r",encoding="utf-8")
# print(farkli_konum.read())

# for i in farkli_konum:
#     print(i)

"""Read ile belirtilen karektere kadar veriyi alma"""

# print(farkli_konum.read(20)) # 20 baytlık veri getirir. Her karakter bir 1 byte eder.

# for i in range(20):
#     karakter = farkli_konum.read(1)
#     if not karakter:
#         break
#     print(karakter)
# farkli_konum.close()

"""Readline:Dosya içerisinde ilk satırı getirir"""

# print(farkli_konum.readline())
# print(farkli_konum.readline())
# print(farkli_konum.readline())
# print(farkli_konum.readline())

# print(farkli_konum.readline(20))
# print(farkli_konum.readline(15))
# print(farkli_konum.readline(100))

"""Readlines:Veriyi liste olarak döndürür"""

liste = farkli_konum.readlines()
print(type(liste))

# print(liste)

# liste.insert(2,"Ali")
# for i in farkli_konum:
#     liste.insert(i)
# print(liste)

print(farkli_konum.readable()) # okunabilir bir veri ise True değilse False

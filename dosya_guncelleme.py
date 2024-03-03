"""      Dosya Başına Veri Ekleme       """

with open("test.txt","r+",encoding="utf-8") as dosya:
    okuma = dosya.read()
    okuma = "Bugün Pazar " + okuma
    dosya.seek(0)
    dosya.write(okuma)


"""      Dosya Sonuna Veri Ekleme       """

with open("test.txt","a",encoding="utf-8") as dosya:
    dosya.write(" Dosya Ekleme")


"""      Dosya Ortasına Veri Ekleme       """

# Alternatif 1
    
dosya_yolu = "test.txt"

# Dosyanın içeriğini oku

with open(dosya_yolu, "r", encoding="utf-8") as dosya:
    dosya_icerigi = dosya.read()

# İstediğiniz konuma veriyi ekleyin (örneğin, dosyanın ortasına)

eklenecek_veri = "Bu veri dosyanın ortasına eklendi.\n"
orta_nokta = len(dosya_icerigi) // 2

dosya_icerigi = dosya_icerigi[:orta_nokta] + eklenecek_veri + dosya_icerigi[orta_nokta:]

# Dosyayı tekrar yazın

with open(dosya_yolu, "w", encoding="utf-8") as dosya:
    dosya.write(dosya_icerigi)

# Alternatif 2

with open("with_kullanimi.txt", "r+", encoding="utf-8") as dosya:
    okuma = dosya.read()
    orta_nokta = len(okuma)//2
    okuma = okuma[:orta_nokta]+" DORUK "+okuma[orta_nokta:]
    dosya.seek(0)
    dosya.truncate() #Bir dosyanın boyutunu belirli bir konumdan başlayarak düzenlemek için kullanılır.
    dosya.write(okuma)
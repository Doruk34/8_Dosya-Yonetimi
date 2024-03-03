import os
from datetime import datetime

def dosya_sil(tarih_limiti):
    # Silinecek dosyaların bulunduğu dizini belirtin
    dizin = r"C:\ProgramData\NebimArchive"

    # Dizindeki tüm dosyaları al
    dosya_listesi = os.listdir(dizin)

    # Tarih limitini belirle (örneğin, 2023-01-01)
    tarih_limiti = datetime(2023, 1, 1)

    # Dosyaları kontrol et ve tarih limitinden eski olanları sil
    for dosya in dosya_listesi:
        dosya_yolu = os.path.join(dizin, dosya)
        dosya_modifikasyon_tarihi = datetime.fromtimestamp(os.path.getmtime(dosya_yolu))

        if dosya_modifikasyon_tarihi < tarih_limiti:
            os.remove(dosya_yolu)
            print(f"{dosya} silindi.")

dosya_sil(0) 

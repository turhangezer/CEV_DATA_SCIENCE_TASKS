import time


class PcLab():
    def __init__(self, sinif_no="B141", kayitli_ogrenciler=["1546524"], kayitli_ogrenci_sayisi=1, bos_masa_sayisi=19, dolu_masa_sayisi=1):
        self.sinif_no = sinif_no
        self.kayitli_ogrenciler = kayitli_ogrenciler
        self.kayitli_ogrenci_sayisi = kayitli_ogrenci_sayisi
        self.bos_masa_sayisi = bos_masa_sayisi
        self.dolu_masa_sayisi = dolu_masa_sayisi

    def bilgi_goster(self):
        print("Sınıf numarası: ", self.sinif_no)
        print("Kayıtlı öğrenci sayısı: ", self.kayitli_ogrenci_sayisi)
        print("Kayıtlı öğrenciler: ", self.kayitli_ogrenciler)
        print("Boş masa sayısı: ", self.bos_masa_sayisi)
        print("Dolu masa sayısı: ", self.dolu_masa_sayisi)


class Ogretmen(PcLab):
    def sinif_degistir(self, sinif_adi):
        print("Sınıf değiştiriliyor...")
        time.sleep(1)
        self.sinif_no = sinif_adi
        print("Sınıf değiştirildi")

    def ogrenci_ekle(self, ogrenci_no):
        if ogrenci_no in self.kayitli_ogrenciler:
            print("Öğrenci zaten var")
        else:

            print("Öğrenci ekleniyor...")
            time.sleep(1)
            self.kayitli_ogrenciler.append(ogrenci_no)
            self.kayitli_ogrenci_sayisi += 1
            print("Öğrenci eklendi.")
            print("Öğrenci listesi: {}".format(self.kayitli_ogrenciler))

    def ogrenci_listele(self):
        print(self.kayitli_ogrenciler)


class Ogrenci(PcLab):
    def masaya_otur(self):
        if (self.bos_masa_sayisi > 0):
            print("Masaya oturuluyor..")
            time.sleep(1)
            self.bos_masa_sayisi -= 1
            self.dolu_masa_sayisi += 1
        else:
            print("Bos masa yok :(")

    def masadan_kalk(self):
        print("Masadan kalkiliyor..")
        time.sleep(1)
        self.dolu_masa_sayisi -= 1
        self.bos_masa_sayisi += 1
        print("Masa boş.")


lab = PcLab()
ogretmen = Ogretmen(PcLab)
ogrenci = Ogrenci(PcLab)
while True:
    secim = input("a-Öğretmen\n\nb-Öğrenci \n")
    if (secim == "a"):

        print("""
            1.Sınıf değiştir
            2.Öğrenci ekle
            3.Öğrenci listele
            4.Bilgileri göster
            5.Çıkış
            
            
            """)

        islem1 = input("Hoşgeldiniz lütfen bir seçim yapınız: ")

        if islem1 == "1":
            sinif_adi = input("Yeni sınıfı giriniz.")
            ogretmen.sinif_degistir(sinif_adi)
        elif islem1 == "2":
            ogrenci_no = input("Öğrenci numarasını giriniz.")
            ogretmen.ogrenci_ekle(ogrenci_no)
        elif islem1 == "3":
            ogretmen.ogrenci_listele()
        elif islem1 == "4":
            lab.bilgi_goster()
        elif islem1 == "5":
            break
        else:
            print("Geçersiz işlem")

    elif (secim == "b"):
        print("""
        1.Masaya otur
        2.Masadan kalk
        3.Bilgileri göster
        4.Çıkış
        """)
        islem2 = input("Hoşgeldiniz lütfen bir seçim yapınız: ")
        if islem2 == "1":
            ogrenci.masaya_otur()
        elif islem2 == "2":
            ogrenci.masadan_kalk()
        elif islem2 == "3":
            ogrenci.bilgi_goster()
        elif islem2 == "4":
            break
        else:
            print("Geçersiz işlem")

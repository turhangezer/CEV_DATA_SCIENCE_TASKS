class Hayvanlar():
    def __init__(self, hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi):
        self.hayvan_turu = hayvan_turu
        self.hayvan_adi = hayvan_adi
        self.hayvan_rengi = hayvan_rengi
        self.hayvan_yasi = hayvan_yasi

    def Bilgi(self):
        print("Hayvan Türü: {}".format(self.hayvan_turu))
        print("Hayvan Adı: {}".format(self.hayvan_adi))
        print("Hayvan Rengi: {}".format(self.hayvan_rengi))
        print("Hayvan Yaşı: {}".format(self.hayvan_yasi))


class Dinazor(Hayvanlar):
    def __init__(self, hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi, dinazor_turu):
        super().__init__(hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi)
        self.dinazor_turu = dinazor_turu

    def Bilgi(self):
        super().Bilgi()
        print("Dinazor Türü: {}".format(self.dinazor_turu))


class Orkinos(Hayvanlar):
    def __init__(self, hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi, orkinos_turu):
        super().__init__(hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi)
        self.orkinos_turu = orkinos_turu

    def Bilgi(self):
        super().Bilgi()
        print("Orkinos Türü: {}".format(self.orkinos_turu))


class Kartal(Hayvanlar):
    def __init__(self, hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi, kartal_turu):
        super().__init__(hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi)
        self.kartal_turu = kartal_turu

    def Bilgi(self):
        super().Bilgi()
        print("Kartal Türü: {}".format(self.kartal_turu))


class Ceylan(Hayvanlar):
    def __init__(self, hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi, ceylan_turu):
        super().__init__(hayvan_turu, hayvan_rengi, hayvan_adi, hayvan_yasi)
        self.ceylan_turu = ceylan_turu

    def Bilgi(self):
        super().Bilgi()
        print("Ceylan Türü: {}".format(self.ceylan_turu))




print(Dinazor("Dinazor", "Kahverengi", "Enzo", 100, "T-Rex").Bilgi())
print(Orkinos("Orkinos", "Siyah", "Laz Ziya", 100, "Uzun Kanat Orkinos").Bilgi())
print(Kartal("Kartal", "Beyaz", "Bald", 100, "Kel Kartal").Bilgi())
print(Ceylan("Ceylan", "Siyah", "Bambi", 100, "Dağ Ceylanı").Bilgi())

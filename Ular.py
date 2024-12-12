from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak()
        print("design \t\t\t: ", self.design,
        "\nracun \t\t\t: ", self.racun,)

anaconda = Ular("anaconda", "tikus", "amazon", "bertelur", "batik solo", "tidak beracun")
anaconda.cetak_ular()

kobra = Ular("kobra", "ayam", "amazon", "bertelur", "hitam", "beracun")
kobra.cetak_ular()
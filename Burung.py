from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis = jenis

    def cetak_Burung(self):
        super().cetak()
        print("warna \t\t\t: ", self.warna,
        "\njenis \t\t\t: ", self.jenis,)

merpati = Burung("merpati", "jagung", "hutan", "bertelur", "putih", "merpati jawa")
merpati.cetak_Burung()

murai = Burung("murai", "pisang", "hutan", "bertelur", "hitam", "luzon filipina")
murai.cetak_Burung()
from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, harga):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.harga = harga

    def cetak_Ikan(self):
        super().cetak()
        print("jenis \t\t\t: ", self.jenis,
        "\nharga \t\t\t: ", self.harga,)

arwana = Ikan("arwana", "jangkrik", "sungai nil", "bertelur", "merah siluk", "11 juta")
arwana.cetak_Ikan()

toman = Ikan("toman", "katak", "danau toba", "bertelur", "chana merulius", "24 juta")
toman.cetak_Ikan()
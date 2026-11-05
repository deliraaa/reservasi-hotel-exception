from kamar import Kamar
from kamar_deluxe import KamarDeluxe

class KamarSuite(KamarDeluxe):
    def __init__(self, nomor_kamar, harga_per_malam):
        super().__init__(nomor_kamar, harga_per_malam)
        self._fasilitas += ["Ruang tamu", "Bathtub"] 

    def deskripsi(self):
        return f"Suite {self.nomor_kamar} - " + Kamar.deskripsi(self)
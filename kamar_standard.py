from kamar import Kamar


class KamarStandard(Kamar):
    def __init__(self, nomor_kamar, harga_per_malam):
        super().__init__(nomor_kamar, harga_per_malam,
                         ["AC", "TV", "Kamar mandi"])

    def deskripsi(self):
        return f"Standard {self.nomor_kamar} - " + super().deskripsi()
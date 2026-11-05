from kamar import Kamar


class KamarDeluxe(Kamar):
    def __init__(self, nomor_kamar, harga_per_malam):
        super().__init__(nomor_kamar, harga_per_malam,
                         ["AC", "TV", "Kamar mandi", "Balkon", "Kulkas mini"])

    def deskripsi(self):
        return f"Deluxe {self.nomor_kamar} - " + super().deskripsi()
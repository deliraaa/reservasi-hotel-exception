from layanan_tambahan import LayananTambahan


class Laundry(LayananTambahan):
    BIAYA_PER_KG = 15000  

    def __init__(self, berat_kg):
        super().__init__("Laundry", Laundry.BIAYA_PER_KG, berat_kg)

    def keterangan(self):
        return f"Laundry {self._jumlah} kg"
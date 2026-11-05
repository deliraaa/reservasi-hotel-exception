from layanan_tambahan import LayananTambahan


class Tagihan:
    def __init__(self, biaya_kamar):
        self.__biaya_kamar = 0
        self.__daftar_layanan = []        
        self.biaya_kamar = biaya_kamar    

    @property
    def biaya_kamar(self):
        return self.__biaya_kamar

    @biaya_kamar.setter
    def biaya_kamar(self, nilai):
        if nilai < 0:
            raise ValueError("Biaya kamar tidak boleh negatif")
        self.__biaya_kamar = nilai

    def tambah_layanan(self, layanan):
        if not isinstance(layanan, LayananTambahan):
            raise TypeError("Yang ditambahkan harus object LayananTambahan")
        self.__daftar_layanan.append(layanan)

    def hitung_biaya_layanan(self):
        return sum(l.hitung_biaya() for l in self.__daftar_layanan)

    def hitung_total(self):
        return self.__biaya_kamar + self.hitung_biaya_layanan()

    def cetak(self):
        baris = [f"{'Biaya kamar':<30} Rp{self.__biaya_kamar:>10,}"]
        for l in self.__daftar_layanan:
            baris.append(f"{l.keterangan():<30} Rp{l.hitung_biaya():>10,}")
        baris.append("-" * 43)
        baris.append(f"{'TOTAL':<30} Rp{self.hitung_total():>10,}")
        return "\n".join(baris)
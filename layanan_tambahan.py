from exceptions import DataTidakValidError


class LayananTambahan:
    def __init__(self, nama, biaya_satuan, jumlah):
        self._nama = nama
        self._biaya_satuan = 0
        self._jumlah = 0
        self.biaya_satuan = biaya_satuan
        self.jumlah = jumlah

    @property
    def biaya_satuan(self):
        return self._biaya_satuan

    @biaya_satuan.setter
    def biaya_satuan(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai <= 0:
            raise DataTidakValidError("Biaya satuan harus lebih dari 0")
        self._biaya_satuan = nilai

    @property
    def jumlah(self):
        return self._jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai <= 0:
            raise DataTidakValidError("Jumlah layanan harus lebih dari 0")
        self._jumlah = nilai

    def hitung_biaya(self):
        return self._biaya_satuan * self._jumlah

    def keterangan(self):
        return f"{self._nama} x{self._jumlah}"

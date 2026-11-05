from layanan_tambahan import LayananTambahan

class RoomService(LayananTambahan):
    def __init__(self, nama_menu, harga, porsi):
        super().__init__(nama_menu, harga, porsi)

    def keterangan(self):
        return f"Room Service {self._nama} x{self._jumlah}"
class HotelError(Exception):
    """Base exception untuk seluruh error sistem reservasi hotel."""

    def __init__(self, pesan="Terjadi kesalahan pada sistem hotel"):
        super().__init__(pesan)
        self.pesan = pesan


class DataTidakValidError(HotelError):
    """Data input tidak valid (harga, telepon, jumlah, nama, dll)."""


class KamarTidakTersediaError(HotelError):
    """Kamar sedang terisi / tidak bisa dipesan."""


class TanggalTidakValidError(HotelError):
    """Tanggal check-in / check-out tidak valid."""


class ReservasiError(HotelError):
    """Aturan reservasi dilanggar (kosong, sudah dibatalkan, dll)."""
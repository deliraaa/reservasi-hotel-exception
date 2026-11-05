from reservasi import Reservasi


class Tamu:
    jumlah_tamu = 0 

    def __init__(self, id_tamu, nama, no_telepon):
        self.__id_tamu = id_tamu
        self.__nama = nama
        self.__no_telepon = None
        self.__daftar_reservasi = []
        self.no_telepon = no_telepon      
        Tamu.jumlah_tamu += 1

    @property
    def id_tamu(self):
        return self.__id_tamu

    @property
    def nama(self):
        return self.__nama

    @property
    def no_telepon(self):
        return self.__no_telepon

    @no_telepon.setter
    def no_telepon(self, nilai):
        if not Tamu.validasi_telepon(nilai):
            raise ValueError("No telepon harus 10-13 digit angka")
        self.__no_telepon = nilai

    @property
    def daftar_reservasi(self):
        return list(self.__daftar_reservasi)

    @staticmethod
    def validasi_telepon(nomor):
        return nomor.isdigit() and 10 <= len(nomor) <= 13

    @classmethod
    def dari_string(cls, teks):
        id_tamu, nama, telepon = teks.split("-")
        return cls(id_tamu, nama, telepon)

    def buat_reservasi(self, daftar_kamar, check_in, check_out):
        reservasi = Reservasi(self, daftar_kamar, check_in, check_out)
        self.__daftar_reservasi.append(reservasi)
        return reservasi

    def __str__(self):
        return f"Tamu[{self.__id_tamu}] {self.__nama} ({self.__no_telepon})"

    def __repr__(self):
        return f"Tamu('{self.__id_tamu}', '{self.__nama}', '{self.__no_telepon}')"

    def __eq__(self, other):
        if not isinstance(other, Tamu):
            return False
        return self.__id_tamu == other.__id_tamu
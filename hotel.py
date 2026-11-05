from kamar import Kamar


class Hotel:
    def __init__(self, nama, alamat):
        self.__nama = nama
        self.__alamat = alamat
        self.__daftar_kamar = []   

    @property
    def nama(self):
        return self.__nama

    def tambah_kamar(self, kamar):
        if not isinstance(kamar, Kamar):
            raise TypeError("Yang ditambahkan harus object Kamar")
        self.__daftar_kamar.append(kamar)

    def cari_kamar_tersedia(self):
        return [k for k in self.__daftar_kamar if k.tersedia]

    def __str__(self):
        return (f"{self.__nama} ({self.__alamat}) - "
                f"{len(self.__daftar_kamar)} kamar")
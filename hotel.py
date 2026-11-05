from kamar import Kamar
from exceptions import DataTidakValidError


class Hotel:
    def __init__(self, nama, alamat):
        if not nama or not nama.strip():
            raise DataTidakValidError("Nama hotel tidak boleh kosong")
        self.__nama = nama
        self.__alamat = alamat
        self.__daftar_kamar = []

    @property
    def nama(self):
        return self.__nama

    def tambah_kamar(self, kamar):
        if not isinstance(kamar, Kamar):
            raise DataTidakValidError("Yang ditambahkan harus object Kamar")
        if any(k.nomor_kamar == kamar.nomor_kamar for k in self.__daftar_kamar):
            raise DataTidakValidError(
                f"Kamar {kamar.nomor_kamar} sudah terdaftar di hotel")
        self.__daftar_kamar.append(kamar)

    def cari_kamar_tersedia(self):
        return [k for k in self.__daftar_kamar if k.tersedia]

    def __str__(self):
        return (f"{self.__nama} ({self.__alamat}) - "
                f"{len(self.__daftar_kamar)} kamar")
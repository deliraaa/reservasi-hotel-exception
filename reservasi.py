from tagihan import Tagihan
from exceptions import (ReservasiError, KamarTidakTersediaError,
                        TanggalTidakValidError)


class Reservasi:
    jumlah_reservasi = 0

    def __init__(self, tamu, daftar_kamar, check_in, check_out):
        if not daftar_kamar:
            raise ReservasiError("Minimal pesan satu kamar")

        nomor = [k.nomor_kamar for k in daftar_kamar]
        if len(nomor) != len(set(nomor)):
            raise ReservasiError("Kamar yang sama tidak boleh dipesan dua kali")

        for k in daftar_kamar:
            if not k.tersedia:
                raise KamarTidakTersediaError(
                    f"Kamar {k.nomor_kamar} tidak tersedia")
        self.__tamu = tamu
        self.__daftar_kamar = list(daftar_kamar)
        self.__check_in = check_in
        self.__check_out = None
        self.check_out = check_out
        self.__status = "Aktif"
        biaya_kamar = sum(k.hitung_biaya(self.lama_menginap)
                          for k in self.__daftar_kamar)

        self.__tagihan = Tagihan(biaya_kamar)
        for k in self.__daftar_kamar:
            k.pesan()
        Reservasi.jumlah_reservasi += 1
        self.__id_reservasi = f"R{Reservasi.jumlah_reservasi:03d}"

    @property
    def tagihan(self):
        return self.__tagihan

    @property
    def status(self):
        return self.__status

    @property
    def check_out(self):
        return self.__check_out

    @check_out.setter
    def check_out(self, nilai):
        if nilai <= self.__check_in:
            raise TanggalTidakValidError(
                "Tanggal check-out harus setelah check-in")
        self.__check_out = nilai

    @property
    def lama_menginap(self):
        return (self.__check_out - self.__check_in).days

    def tambah_layanan(self, layanan):
        if self.__status == "Dibatalkan":
            raise ReservasiError(
                "Tidak bisa menambah layanan pada reservasi yang dibatalkan")
        self.__tagihan.tambah_layanan(layanan)

    def batalkan(self):
        if self.__status == "Dibatalkan":
            raise ReservasiError("Reservasi sudah dibatalkan sebelumnya")
        self.__status = "Dibatalkan"
        for k in self.__daftar_kamar:
            k.kosongkan()

    def __str__(self):
        nomor = ", ".join(k.nomor_kamar for k in self.__daftar_kamar)
        return (f"Reservasi {self.__id_reservasi}: {self.__tamu.nama}, "
                f"kamar {nomor}, {self.lama_menginap} malam, "
                f"status {self.__status}")
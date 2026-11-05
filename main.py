from datetime import date
from hotel import Hotel
from tamu import Tamu
from kamar import Kamar
from reservasi import Reservasi
from kamar_standard import KamarStandard
from kamar_deluxe import KamarDeluxe
from kamar_suite import KamarSuite
from laundry import Laundry
from room_service import RoomService
from exceptions import (HotelError, DataTidakValidError,
                        KamarTidakTersediaError, TanggalTidakValidError,
                        ReservasiError)


def judul(teks):
    print()
    print("=" * 60)
    print(teks)
    print("=" * 60)


if __name__ == "__main__":
    judul("1. DATA HOTEL DAN KAMAR")
    hotel = Hotel("Hotel Bali Asri", "Denpasar, Bali")
    k1 = KamarStandard("101", 400000)
    k2 = KamarDeluxe("201", 700000)
    k3 = KamarSuite("301", 1200000)
    for kamar in (k1, k2, k3):
        hotel.tambah_kamar(kamar)
    print(hotel)
    print(k1)
    print(k2)
    print(k3)

    judul("2. DATA TAMU")
    budi = Tamu.dari_string("T001-Budi Santoso-081234567890")
    sari = Tamu("T002", "Sari Dewi", "085611223344")
    print(budi)
    print(sari)

    judul("3. UJI ATURAN BISNIS (DATA TIDAK VALID)")
    
    try:
        k1.harga_per_malam = -500000
    except DataTidakValidError as e:
        print("[DataTidakValidError] harga = -500000 ->", e)
    else:
        print("Harga berhasil diubah")
    finally:
        print("  (uji harga selesai)")

    try:
        budi.no_telepon = "abc123"
    except DataTidakValidError as e:
        print("[DataTidakValidError] no_telepon = 'abc123' ->", e)
    else:
        print("No telepon berhasil diubah")
    finally:
        print("  (uji telepon selesai)")

    try:
        hotel.tambah_kamar(KamarStandard("101", 350000))
    except DataTidakValidError as e:
        print("[DataTidakValidError] kamar duplikat ->", e)
    else:
        print("Kamar berhasil ditambahkan")
    finally:
        print("  (uji kamar duplikat selesai)")

    judul("4. UJI TANGGAL TIDAK VALID")
    try:
        budi.buat_reservasi([k1], date(2026, 11, 3), date(2026, 11, 1))
    except TanggalTidakValidError as e:
        print("[TanggalTidakValidError] ->", e)
    except HotelError as e:
        print("[HotelError] ->", e)
    else:
        print("Reservasi berhasil dibuat")
    finally:
        print("  (uji tanggal selesai)")

    judul("5. SKENARIO RESERVASI")
    print("Kamar tersedia (awal)      :", len(hotel.cari_kamar_tersedia()))
    r1 = None
    try:
        r1 = budi.buat_reservasi([k1, k2], date(2026, 11, 1), date(2026, 11, 3))
        r1.tambah_layanan(Laundry(3))
        r1.tambah_layanan(RoomService("Nasi Goreng", 45000, 2))
    except KamarTidakTersediaError as e:
        print("[KamarTidakTersediaError] ->", e)
    except ReservasiError as e:
        print("[ReservasiError] ->", e)
    except HotelError as e:
        print("[HotelError] ->", e)
    else:
        print(r1)
        print()
        print("Tagihan:")
        print(r1.tagihan.cetak())
    finally:
        print("Kamar tersedia (dipesan)   :", len(hotel.cari_kamar_tersedia()))

    try:
        sari.buat_reservasi([k1, k3], date(2026, 11, 2), date(2026, 11, 4))
    except KamarTidakTersediaError as e:
        print("[KamarTidakTersediaError] Reservasi ditolak ->", e)
    except HotelError as e:
        print("[HotelError] ->", e)
    else:
        print("Reservasi Sari berhasil")
    finally:
        print("  (uji kamar terisi selesai)")

    try:
        sari.buat_reservasi([], date(2026, 11, 2), date(2026, 11, 4))
    except ReservasiError as e:
        print("[ReservasiError] ->", e)
    finally:
        print("  (uji reservasi kosong selesai)")

    try:
        sari.buat_reservasi([k3, k3], date(2026, 11, 2), date(2026, 11, 4))
    except ReservasiError as e:
        print("[ReservasiError] kamar ganda ->", e)
    finally:
        print("  (uji kamar ganda selesai)")

    try:
        r1.batalkan()
        print(r1)
        r1.batalkan()
    except ReservasiError as e:
        print("[ReservasiError] batal kedua ->", e)
    else:
        print("Pembatalan berhasil")
    finally:
        print("Kamar tersedia (dibatalkan):", len(hotel.cari_kamar_tersedia()))

    try:
        r1.tambah_layanan(Laundry(1))
    except ReservasiError as e:
        print("[ReservasiError] tambah layanan setelah batal ->", e)
    finally:
        print("  (uji tambah layanan selesai)")

    judul("6. CLASS ATTRIBUTE DAN URUTAN CONSTRUCTOR")
    print("Jumlah Tamu      :", Tamu.jumlah_tamu)
    print("Jumlah Kamar     :", Kamar.jumlah_kamar)
    print("Jumlah Reservasi :", Reservasi.jumlah_reservasi)
    print("MRO KamarSuite   :", " -> ".join(c.__name__ for c in KamarSuite.__mro__))
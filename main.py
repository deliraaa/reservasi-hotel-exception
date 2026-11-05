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
    print()
    print(k1)
    print(k2)
    print(k3)

    judul("2. DATA TAMU")
    budi = Tamu.dari_string("T001-Budi Santoso-081234567890")
    sari = Tamu("T002", "Sari Dewi", "085611223344")
    print(budi)
    print(sari)

    judul("3. UJI VALIDASI SETTER")
    try:
        budi.no_telepon = "abc123"
    except ValueError as e:
        print("no_telepon = 'abc123'  ->", e)
    try:
        k1.harga_per_malam = -500000
    except ValueError as e:
        print("harga = -500000        ->", e)

    judul("4. PERBANDINGAN OBJECT (==)")
    budi_lagi = Tamu("T001", "Budi S.", "081200000000")
    print("budi == budi_lagi :", budi == budi_lagi)
    print("budi == sari      :", budi == sari)

    judul("5. SKENARIO RESERVASI")
    print("Kamar tersedia (awal)      :", len(hotel.cari_kamar_tersedia()))
    r1 = budi.buat_reservasi([k1, k2], date(2026, 11, 1), date(2026, 11, 3))
    print(r1)
    r1.tambah_layanan(Laundry(3))
    r1.tambah_layanan(RoomService("Nasi Goreng", 45000, 2))
    print()
    print("Tagihan:")
    print(r1.tagihan.cetak())
    print()
    try:
        sari.buat_reservasi([k1, k3], date(2026, 11, 2), date(2026, 11, 4))
    except ValueError as e:
        print("Reservasi ditolak          :", e)
    print("Kamar tersedia (dipesan)   :", len(hotel.cari_kamar_tersedia()))
    r1.batalkan()
    print(r1)
    print("Kamar tersedia (dibatalkan):", len(hotel.cari_kamar_tersedia()))

    judul("6. CLASS ATTRIBUTE DAN URUTAN CONSTRUCTOR")
    print("Jumlah Tamu      :", Tamu.jumlah_tamu)
    print("Jumlah Kamar     :", Kamar.jumlah_kamar)
    print("Jumlah Reservasi :", Reservasi.jumlah_reservasi)
    print("MRO KamarSuite   :", " -> ".join(c.__name__ for c in KamarSuite.__mro__))
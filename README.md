# Sistem Reservasi Hotel (dengan Exception Handling)

Pengembangan proyek UTS dengan menambahkan exception handling pada studi kasus reservasi hotel.

## Anggota Kelompok

| Nama                         | NIM        | Kontribusi                                |
| ---------------------------- | ---------- | ----------------------------------------- |
| Candra Made Lintang Rakaheni | 2501010011 | reservasi.py, main.py, README.md          |
| Azalea Vidya Kirana          | 2501010014 | exceptions.py, kamar.py, hotel.py         |
| I Made Dhananjaya            | 2501010033 | tamu.py, layanan_tambahan.py, tagihan.py  |

## Aturan Bisnis yang Dapat Dilanggar

| No  | Aturan                                                                                    | Exception               | Lokasi                          |
| --- | ----------------------------------------------------------------------------------------- | ----------------------- | ------------------------------- |
| 1   | Harga kamar, biaya satuan, dan jumlah layanan harus > 0; biaya kamar tidak boleh negatif  | DataTidakValidError     | Kamar, LayananTambahan, Tagihan |
| 2   | No telepon 10-13 digit angka, nama tidak kosong                                           | DataTidakValidError     | Tamu                            |
| 3   | Kamar yang dipesan harus tersedia                                                         | KamarTidakTersediaError | Kamar, Reservasi                |
| 4   | Check-out harus setelah check-in                                                          | TanggalTidakValidError  | Reservasi                       |
| 5   | Minimal 1 kamar; reservasi batal tidak bisa dibatalkan/ditambah layanan lagi              | ReservasiError          | Reservasi                       |
| 6   | Nomor kamar tidak boleh duplikat di hotel                                                 | DataTidakValidError     | Hotel                           |
| 7   | Kamar yang sama tidak boleh dipesan dua kali dalam satu reservasi                         | ReservasiError          | Reservasi                       |

## Hierarki Exception

`HotelError` adalah base exception (turunan `Exception`) dengan empat turunan:
`DataTidakValidError`, `KamarTidakTersediaError`, `TanggalTidakValidError`, dan `ReservasiError`.
Semua didefinisikan di `exceptions.py`.

## Class Diagram

```mermaid
classDiagram
    class Exception
    class HotelError {
        +pesan : str
        +__init__(pesan)
    }
    class DataTidakValidError
    class KamarTidakTersediaError
    class TanggalTidakValidError
    class ReservasiError
    Exception <|-- HotelError
    HotelError <|-- DataTidakValidError
    HotelError <|-- KamarTidakTersediaError
    HotelError <|-- TanggalTidakValidError
    HotelError <|-- ReservasiError

    class Hotel {
        -nama : str
        -alamat : str
        -daftar_kamar : list~Kamar~
        +__init__(nama, alamat)
        +tambah_kamar(kamar) None
        +cari_kamar_tersedia() list~Kamar~
        +__str__() str
    }
    class Kamar {
        +jumlah_kamar : int$
        -nomor_kamar : str
        #harga_per_malam : int
        #fasilitas : list~str~
        -tersedia : bool
        +__init__(nomor_kamar, harga_per_malam, fasilitas)
        +harga_per_malam(nilai) None
        +pesan() None
        +kosongkan() None
        +hitung_biaya(malam) int
        +deskripsi() str
        +__str__() str
    }
    class KamarStandard {
        +__init__(nomor_kamar, harga_per_malam)
        +deskripsi() str
    }
    class KamarDeluxe {
        +__init__(nomor_kamar, harga_per_malam)
        +deskripsi() str
    }
    class KamarSuite {
        +__init__(nomor_kamar, harga_per_malam)
        +deskripsi() str
    }
    Kamar <|-- KamarStandard
    Kamar <|-- KamarDeluxe
    KamarDeluxe <|-- KamarSuite

    class Tamu {
        +jumlah_tamu : int$
        -id_tamu : str
        -nama : str
        -no_telepon : str
        -daftar_reservasi : list~Reservasi~
        +__init__(id_tamu, nama, no_telepon)
        +no_telepon(nilai) None
        +buat_reservasi(daftar_kamar, check_in, check_out) Reservasi
        +validasi_telepon(nomor) bool$
        +dari_string(teks) Tamu$
        +__str__() str
        +__repr__() str
        +__eq__(other) bool
    }
    class Reservasi {
        +jumlah_reservasi : int$
        -id_reservasi : str
        -tamu : Tamu
        -daftar_kamar : list~Kamar~
        -check_in : date
        -check_out : date
        -status : str
        -tagihan : Tagihan
        +__init__(tamu, daftar_kamar, check_in, check_out)
        +check_out(nilai) None
        +lama_menginap() int
        +tambah_layanan(layanan) None
        +batalkan() None
        +__str__() str
    }
    class Tagihan {
        -biaya_kamar : int
        -daftar_layanan : list~LayananTambahan~
        +__init__(biaya_kamar)
        +biaya_kamar(nilai) None
        +tambah_layanan(layanan) None
        +hitung_biaya_layanan() int
        +hitung_total() int
        +cetak() str
    }
    class LayananTambahan {
        #nama : str
        #biaya_satuan : int
        #jumlah : int
        +__init__(nama, biaya_satuan, jumlah)
        +biaya_satuan(nilai) None
        +jumlah(nilai) None
        +hitung_biaya() int
        +keterangan() str
    }
    class Laundry {
        +BIAYA_PER_KG : int$
        +__init__(berat_kg)
        +keterangan() str
    }
    class RoomService {
        +__init__(nama_menu, harga, porsi)
        +keterangan() str
    }
    LayananTambahan <|-- Laundry
    LayananTambahan <|-- RoomService

    Hotel "1" *-- "1..*" Kamar
    Tamu "1" --> "0..*" Reservasi
    Reservasi "0..*" --> "1..*" Kamar
    Reservasi "1" *-- "1" Tagihan
    Tagihan "1" o-- "0..*" LayananTambahan

    Kamar ..> DataTidakValidError : raise
    Kamar ..> KamarTidakTersediaError : raise
    Hotel ..> DataTidakValidError : raise
    Tamu ..> DataTidakValidError : raise
    LayananTambahan ..> DataTidakValidError : raise
    Tagihan ..> DataTidakValidError : raise
    Reservasi ..> KamarTidakTersediaError : raise
    Reservasi ..> TanggalTidakValidError : raise
    Reservasi ..> ReservasiError : raise
```

## Penanganan Exception di Program Utama

`main.py` menggunakan blok `try`, `except` (dari yang spesifik ke umum), `else`, dan `finally`
untuk menguji setiap aturan bisnis di atas.

## Cara Menjalankan

```bash
python main.py
```
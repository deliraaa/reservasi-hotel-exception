class Kamar:
    jumlah_kamar = 0  

    def __init__(self, nomor_kamar, harga_per_malam, fasilitas):
        self.__nomor_kamar = nomor_kamar     
        self._harga_per_malam = 0            
        self._fasilitas = list(fasilitas)     
        self.__tersedia = True                
        self.harga_per_malam = harga_per_malam  
        Kamar.jumlah_kamar += 1

    @property
    def nomor_kamar(self):
        
        return self.__nomor_kamar

    @property
    def harga_per_malam(self):
        return self._harga_per_malam

    @harga_per_malam.setter
    def harga_per_malam(self, nilai):
        if nilai <= 0:
            raise ValueError("Harga per malam harus lebih dari 0")
        self._harga_per_malam = nilai

    @property
    def tersedia(self):
        return self.__tersedia

    def pesan(self):
        self.__tersedia = False

    def kosongkan(self):
        self.__tersedia = True

    def hitung_biaya(self, malam):
        return self._harga_per_malam * malam

    def deskripsi(self):
        return "fasilitas: " + ", ".join(self._fasilitas)

    def __str__(self):
        status = "Tersedia" if self.__tersedia else "Terisi"
        return (f"{self.deskripsi()}\n"
                f"   Harga: Rp{self._harga_per_malam:,}/malam | Status: {status}")
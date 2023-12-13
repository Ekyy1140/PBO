class Animal:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.nama = nama  
        self.sifat = sifat  
        self.ukuran = ukuran  
        self._jumlah_kaki = jumlah_kaki  

    def identifikasi(self):
        print(f"{self.nama} adalah sejenis hewan dengan sifat {self.sifat}, ukuran {self.ukuran}, dan memiliki {self._jumlah_kaki} kaki.")

    def bersuara(self, suara="Bunyi umum hewan"):
        print(f"{self.nama} bersuara: {suara}")


class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self._bisa_jalan = bisa_jalan  
        self._jenis_mamalia = jenis_mamalia  

    def identifikasi(self):
        super().identifikasi()
        print(f"Termasuk dalam jenis mamalia, bisa jalan: {self._bisa_jalan}, jenis mamalia: {self._jenis_mamalia}")

    def bersuara(self, suara="Bunyi mamalia"):
        print(f"{self.nama} bersuara: {suara}")

    def get_jenis_mamalia(self):
        return self._jenis_mamalia


class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self._bisa_terbang = bisa_terbang  
        self._jenis_aves = jenis_aves  

    def identifikasi(self):
        super().identifikasi()
        print(f"Termasuk dalam jenis aves, bisa terbang: {self._bisa_terbang}, jenis aves: {self._jenis_aves}")

    def bersuara(self, suara="Kwak...kwak...kwak!"):
        print(f"{self.nama} bersuara: {suara}")

    def get_jenis_aves(self):
        return self._jenis_aves


class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self._jenis_ayam = jenis_ayam  
        self._bisa_diadu = bisa_diadu  

    def identifikasi(self):
        super().identifikasi()
        print(f"Termasuk dalam jenis ayam, jenis ayam: {self._jenis_ayam}, bisa diadu: {self._bisa_diadu}")

    def bersuara(self, suara="kukuruyuk!!"):
        print(f"{self.nama} bersuara: {suara}")

    def get_jenis_ayam(self):
        return self._jenis_ayam

    def get_bisa_diadu(self):
        return self._bisa_diadu


class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
    def bersuara(self, suara="kur-kur kuk geruk!!"):
        print(f"{self.nama} bersuara: {suara}")

singa = Mamalia("Singa", "Buas", "Besar", 4, True, "Karnivora")
kuda = Mamalia("Kuda", "Penurut", "Sedang", 4, True, "Herbivora")
gajah = Mamalia("Gajah", "Kalem", "Besar", 4, True, "Herbivora")
merpati = Merpati("Merpati", "Ramah", "Kecil", 2, True, "Biji-bijian/Granivora")
camar = Aves("Camar", "Ceria", "Kecil", 2, True, "Omnivora/Oportunistik")
ayam = Ayam("Ayam", "Peternak", "Sedang", 2, True, "Omnivora", "Betina", True)


print()
print(100*'=')
print('\t\t\t\t1. KATEGORI HEWAN MAMALIA')
print(100*'-')
singa.identifikasi()
singa.bersuara()
print('AKSES ATRIBUT PROTECTED DENGAN GETTER:')
print(f"Jenis Mamalia: {singa.get_jenis_mamalia()}")
print()
kuda.identifikasi()
kuda.bersuara()
print()
gajah.identifikasi()
gajah.bersuara()
print(100*'=')
print()

print(100*'=')
print('\t\t\t\t2. KATEGORI HEWAN AVES')
print(100*'-')
camar.identifikasi()
camar.bersuara()
print(100*'=')
print()

print(100*'=')
print('\t\t\t\t3. KATEGORI HEWAN AYAM')
print(100*'-')
ayam.identifikasi()
ayam.bersuara()
print()
print('AKSES ATRIBUT PROTECTED DENGAN GETTER:')
print(f"Jenis Ayam: {ayam.get_jenis_ayam()}")
print(f"Bisa Diadu: {ayam.get_bisa_diadu()}")
print(100*'=')

print()
print(100*'=')
print('\t\t\t\t4. KATEGORI HEWAN MERPATI')
print(100*'-')
merpati.identifikasi()
merpati.bersuara()
print(100*'=')

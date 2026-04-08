class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan

class MahasiswaAktif(Mahasiswa):
    def __init__(self, nama, umur, nim, jurusan, jumlah_UKM):
        super().__init__(nama, umur, nim, jurusan)
        self.jumlah_UKM = jumlah_UKM

class MahasiswaTidakAktif(Mahasiswa):
    def __init__(self, nama, umur, nim, jurusan, AlasanTidakAktif):
        super().__init__(nama, umur, nim, jurusan)
        self.AlasanTidakAktif = AlasanTidakAktif

# Contoh penggunaan
if __name__ == "__main__":
    mhs_aktif = MahasiswaAktif("Budi", 20, "123456", "Informatika", 3)
    print(f"Nama: {mhs_aktif.nama}, UKM: {mhs_aktif.jumlah_UKM}")

    mhs_tidak_aktif = MahasiswaTidakAktif("Santi", 21, "654321", "Sistem Informasi", "Cuti Semester")
    print(f"Nama: {mhs_tidak_aktif.nama}, Alasan: {mhs_tidak_aktif.AlasanTidakAktif}")

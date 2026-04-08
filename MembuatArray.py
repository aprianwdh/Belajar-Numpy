class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, nim,jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan

    


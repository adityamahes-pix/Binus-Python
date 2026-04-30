#1

class Siswa:
    
    def __init__(self, nama="Siswa", usia=0, jurusan="Jurusan"):
        self.nama = nama
        self.usia = usia
        self.jurusan = jurusan
    
    def tampilBiodata(self):
        print("Nama    :", self.nama)
        print("usia    :", self.usia)
        print("Jurusan :", self.jurusan)

nama = input("Masukkan Nama Kamu: ")
usia = int(input("Masukkan Usia Kamu: "))
jurusan = input("Masukkan Jurusan Kamu: ")

siswa1 = Siswa(nama, usia, jurusan)
print("\nBiodata Siswa")
siswa1.tampilBiodata()
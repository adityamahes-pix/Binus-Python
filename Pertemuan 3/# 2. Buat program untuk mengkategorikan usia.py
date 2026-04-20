# 2. Buat program untuk mengkategorikan input usia yang diberikan oleh pengguna (input usia tidak boleh negatif).


usia = int(input("Masukkan usia: "))

if usia < 0:
    print("Usia tidak boleh negatif, harap masukkan ulang")
elif usia <= 1:
    print("Kategori usia: Bayi")
elif usia <= 3:
    print("Kategori usia: Balita")
elif usia <= 5:
    print("Kategori usia: Prasekolah")
elif usia <= 12:
    print("Kategori usia: Anak")
elif usia <= 17:
    print("Kategori usia: Remaja")
elif usia <= 21:
    print("Kategori usia: Muda")
elif usia <= 30:
    print("Kategori usia: Pra-dewasa")
elif usia <= 50:
    print("Kategori usia: Dewasa")
elif usia <= 70:
    print("Kategori usia: Pra-lansia")
else:
    print("Kategori usia: Lansia")
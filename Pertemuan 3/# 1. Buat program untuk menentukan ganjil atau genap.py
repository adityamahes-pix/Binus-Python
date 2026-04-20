# 1. Buat program untuk menentukan apakah suatu angka ganjil atau genap berdasarkan input pengguna.


angka = int(input("Masukkan angka: "))

if angka % 2 == 0:
    hasil = "genap"

else:
    hasil = "ganjil"

print("Angka", angka, "adalah", hasil)

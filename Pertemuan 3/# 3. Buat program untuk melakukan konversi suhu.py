# 3. Buat program untuk melakukan konversi suhu:


print("===== Konversi Suhu =====")
print("1. Celcius ke Fahrenheit")
print("2. Celcius ke Kelvin")
print("3. Fahrenheit ke Celcius")
print("4. Fahrenheit ke Kelvin")
print("5. Kelvin ke Celcius")
print("6. Kelvin ke Fahrenheit")
print("=======================")
print()

opsiKonversi = int(input("Pilih opsi konversi suhu (1-6): "))
suhu = float(input("Masukkan suhu: "))

if opsiKonversi == 1:
    hasil = (9/5 * suhu) + 32
    print("Hasil:", hasil, "Fahrenheit")

elif opsiKonversi == 2:
    hasil = suhu + 273
    print("Hasil:", hasil, "Kelvin")

elif opsiKonversi == 3:
    hasil = (5/9) * (suhu - 32)
    print("Hasil:", hasil, "Celcius")

elif opsiKonversi == 4:
    hasil = (5/9) * (suhu - 32) + 273
    print("Hasil:", hasil, "Kelvin")

elif opsiKonversi == 5:
    hasil = suhu - 273
    print("Hasil:", hasil, "Celcius")

elif opsiKonversi == 6:
    hasil = (9/5) * (suhu - 273) + 32
    print("Hasil:", hasil, "Fahrenheit")

else:
    print("Opsi konversi suhu tidak valid")
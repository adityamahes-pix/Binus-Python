3. Buatlah Program untuk menghitung Volume Tabung, jari-jari beserta tinggi diinput oleh user, serta konversikan rumus volumenya menggunakan operator aritmatika. (estimasi 10 menit)


jariJari = int(input("Jari-jari: "))
tinggi = int(input("Tinggi: "))

pi = 3.14
volumeTabung = pi * (jariJari ** 2) * tinggi

print("Volume tabung adalah:", volumeTabung, "meter kubik")

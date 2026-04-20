# 4. Buat program untuk menentukan jenis segitiga berdasarkan panjang tiga sisinya, yang dimasukkan oleh pengguna.


a = float(input("Masukkan sisi A: "))
b = float(input("Masukkan sisi B: "))
c = float(input("Masukkan sisi C: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Bukan Segitiga")
else:

    if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
        print("Segitiga Sudut Kanan")
    elif a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or b == c or a == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Skalen")
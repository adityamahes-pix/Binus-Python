# 5. Buat program percabangan untuk menentukan solusi persamaan kuadrat menggunakan diskriminan.


import math

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("Ini bukan persamaan kuadrat")
else:
    D = b*b - 4*a*c

    if D > 0:
        print("Ini memiliki akar yang berbeda")
        print("Persamaan:", a, "x^2 +", b, "x +", c, "= 0")
        print("Diskriminan:", D)
        print("x1 =", (-b + math.sqrt(D)) / (2*a))
        print("x2 =", (-b - math.sqrt(D)) / (2*a))

    elif D == 0:
        print("Ini memiliki akar ganda")
        print("Persamaan:", a, "x^2 +", b, "x +", c, "= 0")
        print("Diskriminan:", D)
        print("x =", -b / (2*a))

    else:
        print("Ini memiliki akar imajiner")
        print("Persamaan:", a, "x^2 +", b, "x +", c, "= 0")
        print("Diskriminan:", D)
        print("x1 =", (-b/(2*a)), "+", math.sqrt(-D)/(2*a), "i")
        print("x2 =", (-b/(2*a)), "-", math.sqrt(-D)/(2*a), "i")
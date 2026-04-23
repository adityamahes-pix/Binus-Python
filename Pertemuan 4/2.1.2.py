2.1.2

n = int(input("Input Max Value: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

for i in range(2, n+1):
    for j in range(i):
        print(i, end="")
    print()
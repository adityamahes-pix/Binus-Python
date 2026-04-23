2.1.1

n = int(input("input max value: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(i, end="")
    print()
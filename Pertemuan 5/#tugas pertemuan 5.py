#tugas pertemuan 5

def printIntro():
    print("---------------------")
    print("|    Aditya Mahes   |")
    print("|    Bekasinggris   |")
    print("---------------------")

def tambah(a=5, b=5):
    return a + b

def kurang(a=5, b=5):
    return a - b

def kali(a=5, b=5):
    return a * b

def bagi(a=5, b=5):
    return a / b

def modulus(a=5, b=5):
    return a % b

printIntro()

while(True):
    menu = input("Enter Menu (+|-|/|*|%|stop): ")
    if(menu == "stop"):
        print("Program stopped. Thank you for using my program.")
        break
    
    elif(menu == "+" or menu == "-" or menu == "/" or menu == "*" or menu == "%"):
        a = int(input("Enter Value 1: "))
        b = int(input("Enter Value 2: "))
        
	if(menu == "+"):
            result = tambah(a, b)
            print("Result:", result)

        elif(menu == "-"):
            result = kurang(a, b)
            print("Result:", result)

        elif(menu == "*"):
            result = kali(a, b)
            print("Result:", result)

        elif(menu == "/"):
            result = bagi(a, b)
            print("Result:", result)

        elif(menu == "%"):
            result = modulus(a, b)
            print("Result:", result)

    else:
        print("Wrong Menu")
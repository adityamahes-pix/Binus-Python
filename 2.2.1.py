2.2.1

while(True):
    angka = int(input("Enter any number: "))
    
    if (angka % 2 == 0):
        print("The number", angka, "is even")
    else:
        print("The number", angka, "is odd")
    
    ulang = input("Do you want to repeat? (Y/N): ")
    
    if (ulang == "Y" or ulang == "y"):
        continue
    else:
        print("Program Stops")
        print("Thank you for using my program ^^")
        break
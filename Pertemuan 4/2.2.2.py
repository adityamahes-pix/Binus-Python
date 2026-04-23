2.2.2

while(True):
    
    a = float(input("Enter Side A: "))
    b = float(input("Enter Side B: "))
    c = float(input("Enter Side C: "))
    
    if (a + b <= c or a + c <= b or b + c <= a):
        print("It is not a Triangle")
    elif (a == b and b == c):
        print("It is an Equilateral Triangle")
    elif (a == b or b == c or a == c):
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")
    
    while(True):
        ulang = input("Do you want to repeat? (Y/N): ")
        
        if (ulang == "Y" or ulang == "y"):
            break
        elif (ulang == "N" or ulang == "n"):
            print("Program Stops")
            print("Thank you for using my program ^^")
            break
        else:
            print("Input must be Y or N only!")
    
    if (ulang == "N" or ulang == "n"):
        break
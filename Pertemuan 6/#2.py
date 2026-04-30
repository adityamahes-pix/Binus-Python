#2

class Student:
    
    def __init__(self, name="None", score="None"):
        self.name = name
        self.score = score

    def printStudent(self):
        print("Name:", self.name, "\nScore:", self.score)

    def getStudent(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "Score":
            return self.score
       
    def setStudent(self, name, score):
        self.name = name
        self.score = score


student1 = Student()

while(True):
    print("===== OOP Program =====")
    print("1. Declare Object")
    print("2. Display Object")
    print("3. Change Object Value")
    print("4. Delete Object")
    print("5. Exit Program")

    menu = input("Enter Your Choice (1/2/3/4/5): ")

    if(menu == "1"):
        name = input("Enter Your Name: ")
        score = input("Enter Your Score: ")

        student1.setStudent(name, score)
        print("Data Successfully Added")

    elif(menu == "2"):
        print("")
        student1.printStudent()

    elif(menu == "3"):
        choose = input("What would you like to change (Name/Score): ")

        if(choose == "Name"):
            newName = input("Enter New Name: ")
            student1.setStudent(newName, student1.getStudent("Score"))
            print("Name Data Successfully Changed")

        elif(choose == "Score"):
            newScore = input("Enter New Score: ")
            student1.setStudent(student1.getStudent("Name"), newScore)
            print("Score Data Successfully Changed")

        else:
            print("Wrong Input")

    elif(menu == "4"):
        student1.setStudent("None", "None")
        print("Data Successfully Deleted")

    elif(menu == "5"):
        print("Thank you for using my program.")
        break

    else:
        print("Wrong Menu")

    print("")
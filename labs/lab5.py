__author__ = 'Fernando Ames'

#  This program is going to calculate the gpa of the user.

#  Input List: name,courses, grades, g_number
#  Output List: name,gpa, courses

# This program will calculate the final gpa

#   Input Lists: name, g_number, classes, grades
#   Output Lists: name, classes, gpa

# input Lists
# String classes []
# String grades []

classes = []
grades = []


#   Function introduction()
#        Display name = "Please type your name: "
#        Input name
#        Display ("...")
#        Display (".....")
#        Display ("........loading, please wait!........")
#        Display ("Welcome! " + name + ' ' "to the gpa calculator")
#        return name
#    End Function


def introduction():
    name = input("Please type your name: ")
    g_number = input("Please type your G-Number: ")
    print("...")
    print(".....")
    print("........loading, please wait!........")
    print("Welcome! " + name + ' ' "to the gpa calculator")
    return name


#    Function Integer collect(String name)
#        Set i = 0
#        while i < 3:
#              class_name = input("Please " + name + "type your Classes Name: ")
#              classes.append(class_name)
#              i = i + 1
#        Display (classes)
#
#        Set y = 0
#        While y < 3:
#              grade = input("Please " + name + "type your Grade For Each Class Listed in Order (Letter Form): ")
#              grade = grade.upper()
#              grades.append(grade)
#              y = y + 1
#
#       Display (grades)
#    End Function

def collect(name):
    i = 0
    while i < 4:
        class_name = input("Please " + name + "type your Classes Name: ")
        classes.append(class_name)
        i = i + 1

    print(classes)

    y = 0
    while y < 4:
        grade = input("Please " + name + "type your Grade For Each Class Listed in Order (Letter Form): ")
        grade = grade.upper()
        grades.append(grade)
        y = y + 1

    print(grades)


#    Function Integer Calculate():
#        Set total = 0
#            for element in grades:
#                if element == "A+":
#                    total = total + 4.0
#                elif element == "A":
#                      total = total + 4.0
#                elif element == "A-":
#                      total = total + 3.7
#                elif element == "B+":
#                      total = total + 3.3
#                elif element == "B":
#                      total = total + 3.0
#                elif element == "B-":
#                      total = total + 2.7
#                elif element == "C+":
#                      total = total + 2.3
#                elif element == "C":
#                      total = total + 2.0
#                elif element == "C-":
#                      total = total + 1.7
#                elif element == "D":
#                      total = total + 1.0
#            gpa = total / 6
#            Display ("Your Calculated GPA is: ", gpa)
#
def calculate():
    total = 0
    for element in grades:
        if element == "A+":
            total = total + 4.0
        elif element == "A":
            total = total + 4.0
        elif element == "A-":
            total = total + 3.7
        elif element == "B+":
            total = total + 3.3
        elif element == "B":
            total = total + 3.0
        elif element == "B-":
            total = total + 2.7
        elif element == "C+":
            total = total + 2.3
        elif element == "C":
            total = total + 2.0
        elif element == "C-":
            total = total + 1.7
        elif element == "D":
            total = total + 1.0
    gpa = total / 6
    print("Your Calculated GPA is: ", gpa)


#    Function main():
#    Set name = ""
#
#    Call introduction()
#    Call collect(name)
#    Call calculate()
#  End Module

def main():
    name = ""

    introduction()
    collect(name)
    calculate()


main()





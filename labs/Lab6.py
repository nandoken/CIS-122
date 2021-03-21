__author__ = 'Fernando Ames'

# This program will calculate the gpa of the input students.
#
# Input Lists: name, currently_grade, class_name, grade
# Output Lists: name, class_name, gpa
#
# Constant Integer MAX_STUDENTS = 30

MAX_STUDENTS = 30


#  Class Student:
#      Private Integer _number_of_students = 0
#      Private Students _students = [None for x in range(MAX_STUDENTS)]
#      Private Real _gpa = 0.0
#
#      Public Module get_students()
#          Declare Boolean done = False
#          Declare Course course
#          Declare Boolean is_high_school = False
#
#          While not done:
#             Set is_high_school = yes_or_no("Is the student currently in High School (Y/N) ? ")
#             if is_high_school:
#                 Set  course = HighSchool()
#             else:
#                 Set course = College()
#             End if
#             Call course.input()
#             Set  self._students[self._number_of_students] = course
#             Set  self._number_of_students = self._number_of_students + 1
#             Set  done = yes_or_no("Are you finished entering students grades (Y/N) ")
#          End While
#      End Function
#
#      Public Module display()
#          Declare Integer counter = 0
#          Declare Course course
#
#          while counter < _number_of_students:
#              Set course = self._students[counter]
#              Display ("Student: ", (counter + 1), " - ", course.get_name(), " was in the following class: ",
#                   course.get_class_name(), " and the course gpa is: ", self._gpa)
#              Set counter = counter + 1
#          End While
#      End Module
#
#      Public Module calculating_gpa()
#          Declare Integer counter = 0
#          Declare Course course
#          Declare Real total = 0.0
#
#          while counter < _number_of_students:
#              Set course = self._students[counter]
#              if course.get_grade() >= 90:
#                  total = total + 4.0
#              elif course.get_grade() >= 80:
#                  total = total + 3.0
#              elif course.get_grade() >= 70:
#                  total = total + 2.0
#              Set counter = counter + 1
#          Set self._gpa = total / 1
#          End While
#      End Function
#


class Student:
    _number_of_students = 0
    _students = [None for x in range(MAX_STUDENTS)]
    _gpa = 0.0

    def get_students(self):
        done = False
        course = None
        is_high_school = False

        while not done:
            is_high_school = yes_or_no("Is the student currently in High School (Y/N) ? ")
            if is_high_school:
                course = HighSchool()
            else:
                course = College()
            course.input()
            self._students[self._number_of_students] = course
            self._number_of_students = self._number_of_students + 1
            done = yes_or_no("Are you finished entering students grades (Y/N) ")

    def display(self):
        counter = 0
        course = None

        while counter < self._number_of_students:
            course = self._students[counter]
            print("Student: ", (counter + 1), " - ", course.get_name(), " was in the following class: ",
                  course.get_class_name(), " and the course gpa is: ", self._gpa)
            counter = counter + 1

    def calculating_gpa(self):
        counter = 0
        course = None
        total = 0.0

        while counter < self._number_of_students:
            course = self._students[counter]
            if course.get_grade() >= 90:
                total = total + 4.0
            elif course.get_grade() >= 80:
                total = total + 3.0
            elif course.get_grade() >= 70:
                total = total + 2.0
            counter = counter + 1
        self._gpa = total / 1


#  Class HighSchool:
#      Private String _name = ""
#      Private Integer _currently_grade = 0
#      Private String _class_name = ""
#      Private Integer _grade = 0
#
#      Public Module input():
#          Set _name = get_string("Welcome Instructor, Please enter the student full name: ")
#          Set _currently_grade = get_string("Please type " + self._name + " currently High school grade: ")
#          Set _class_name = get_string("Please type " + self._name + " currently High School course name: ")
#          Set _grade = get_real("Please type " + self._name + " final number grade: ")
#      End Module
#
#      Public Function String get_name():
#          Return self._name
#      End Function
#
#      Public Function String get_class_name():
#          Return self._class_name
#      End Function
#
#      Public Integer get_grade():
#          Return self._grade
#      End Function
#  End Class

class HighSchool:
    _name = ""
    _currently_grade = 0
    _class_name = ""
    _grade = 0

    def input(self):
        self._name = get_string("Welcome Instructor, Please enter the student full name: ")
        self._currently_grade = get_string("Please type " + self._name + " currently High school grade: ")
        self._class_name = get_string("Please type " + self._name + " currently High School course name: ")
        self._grade = get_real("Please type " + self._name + " final number grade: ")

    def get_name(self):
        return self._name

    def get_class_name(self):
        return self._class_name

    def get_grade(self):
        return self._grade


#  Class College Extends HighSchool:
#
#     Public Module input():
#         Set _name = get_string("Welcome Instructor! Please type the college student full name: ")
#         Set _class_name = get_string("Please type " + self._name + " currently college course : ")
#         Set _grade = get_real("Please enter " + self._name + " final number grade: ")
#     End Module
#  End Class

class College(HighSchool):

    def input(self):
        self._name = get_string("Welcome Instructor! Please type the college student full name: ")
        self._class_name = get_string("Please type " + self._name + " currently college course : ")
        self._grade = get_real("Please enter " + self._name + " final number grade: ")


#  Function String get_string(String prompt)
#       Declare String value
#
#       Display prompt
#       Input value
#       Return value
#  End Function

def get_string(prompt):
    value = ""

    value = input(prompt)
    return value


#  Function Real get_real(String prompt)
#       Declare String value
#
#       Display prompt
#       Input value
#       While not value is a real number
#           Display value, "is not a number. Please try again."
#           Display prompt
#           Input value
#       End While
#       Return value
#  End Function

def valid_real(value):
    try:
        float(value)
        return True
    except:
        return False


def get_real(prompt):
    value = ""

    value = input(prompt)
    while not valid_real(value):
        print(value, "is not a number. Please type a number and try again. ")
        value = input(prompt)
    return float(value)


#  Function Boolean y_or_n(String prompt)
#       Declare String value
#
#       Display prompt
#       Input value
#       While True
#           If  value == "Y" Or value == "y" Then
#               Return True
#           Else If value == "N" Or value == "n" Then
#               Return False
#           Else
#               Display "Please enter Y or N!"
#               Display prompt
#               Input value
#           End If
#       End While
#  End Function

def yes_or_no(prompt):
    value = ""

    value = input(prompt)
    while True:
        if value == "Y" or value == "y":
            return True
        elif value == "N" or value == "n":
            return False
        else:
            print("Please enter Y or N! ")
            value = input(prompt)


#  Module student_info():
#      Declare Student student
#
#      Set student = New Student()
#      Call student.get_students()
#      Call student.calculating_gpa()
#      Call student.display()
#
#  End Module


def student_info():
    student = None

    student = Student()
    student.get_students()
    student.calculating_gpa()
    student.display()


student_info()

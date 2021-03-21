__author__ = 'Fernando Ames'


# This program asks the user to enter a positive natural number and find whether it is
# an even or odd number after that it finds the factorial of that number

# Input Variable: num
# Output Variable: factorial, number

# Module introduction()
# Set num = input("Please enter a positive natural number to check whether it is even or odd: ")
#     while not num.isdigit() or num== '0':
# Display "Please Enter a positive natural number. Negative, floating numbers and zero are not allowed"
# return eval(num)

def introduction():
    num = input("Please Enter a positive natural number to check whether it is even or odd: ")
    while not num.isdigit() or num == '0':
        num = input("Please Enter a positive natural number. Negative, floating numbers and zero are not allowed")
    return eval(num)


# Function Real finding_the_factorial(Real num)
# Declare factorial = 1
#         for i in range(1, num+1):
#             factorial *= i
#         return factorial
# End Function

def finding_the_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


# Function Real checking_input_number(Real factorial, Real number)
#   if number % 2 == 0 Then
#      print("The number", number,"is an even number.")
#   else:
#      print("The number", number, "is an odd number.")
#   Display ("The factorial of the number", number,"is", factorial)
# End Function

def checking_input_number(factorial, number):
    if number % 2 == 0:
        print("The number", number, "is an even number.")
    else:
        print("The number", number, "is an odd number.")

    print("The factorial of the number", number, "is:", factorial)


# Module main
#
#  Set number = introduction()
#  Set fact = finding_the_factorial(number)
#  Call checking_input_number(factorial, number)
# End Module

def main():
    number = introduction()
    factorial = finding_the_factorial(number)
    checking_input_number(factorial, number)


main()

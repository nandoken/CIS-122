__author__ = 'Fernando Ames'

# This program will do the following:
# 1.Convert Celsius to Fahrenheit.
# 2.Convert Liters to Gallons.
# 3.Calculate the number of days in certain number of seconds and vice versa.
# 4.Calculate the final price of an item after discount and shipping.
#
# Input list: name, option_list, temperature, liters, days, item_price, location_of_the_user
# Output list: name, option_list, temperature, fahrenheit, liters, gallons, days, seconds, item_price, location_of_the_user
#
# Declare string name
# Declare int option_list
# Declare float temperature
# Declare int liters
# Declare int days
# Declare int item_price
# Declare string location_of_the_user
#
# Display "What is your name?"
# Display "Hello (name)! Welcome Please Choose an Option"
# Display "Option List"
# Input option_list
#
# Display option list 1 "Celsius to Fahrenheit Converter"
# Display "Please enter the temperature in Celsius"
# Input temperature
# Set fahrenheit = temperature * (9/5) +32
# Display temperature "degrees Celsius = " , fahrenheit, " degrees Fahrenheit"
#
# Display option list 2 "Liters to Gallons Converter"
# Display "Please enter the number of liters"
# Input liters
# Set gallons = liters * 0.26417205236
# Display liters, "Liters = ", gallons, " Gallons"
#
# Display option list 3 "Number of days to seconds"
# Display "Please enter the number of days"
# Input days
# Set seconds = days * 86400
# Display "{} days are equal to {} seconds" .format(days, seconds)
#
# Display option list 4 "Final price of an item after discount and shipping"
# Display "Please enter your item price"
# Input item_price
# Display "Type West or East to calculate the shipping cost"
# Input location_of_the_user
# Set less_fifty = item_price <= 50
# Set less_than_one_hundred = 50.01 <= item_price <= 100
# Set less_than_one_hundred_and_fifty = 100.01 <= item_price <= 150
# Set beyond_one_hundred_and_fifty = item_price
#
# Set if location_of_the_user is "West"
# Set if item_price <= 50 add shipping cost of $6
# Set if item_price >= 50.01 and <= 100 add shipping cost of $8
# Set if item_price >= 100.01 and <= 150 add shipping cost of $10
# Set if item_price >= 150.01 there is no shipping cost
#
# Set if location_of_the_user is "East"\
# Set if item_price <= 50 add shipping cost of $3
# Set if item_price >= 50.01 and <= 100 and shipping cost of $6
# Set if item_price >= 100.01 and <= 150 add shipping cost of $9
# Set if item_price >= 150.01 there is no shipping cost
#
# Set if option_list #5 is selected
# Display "Thank", name + ''" for using my program!""\nEnd of the Program"
# Set break

while True:
    name = str(input("What is your name?"))
    print("Hello, ", name + '' "! Welcome Please Choose an option:")
    print("1. Convert Celsius to Fahrenheit\n2. Convert Liters to Gallons\n3. Calculate the number of days in "
          "seconds\n4. Calculate the final price of an item after discount and shipping")
    option_list = int(input("5. Exit\nChoose your option: "))

    if option_list == 1:
        print("*****Celsius to Fahrenheit Converter*****")
        temperature = float(input("Please enter the temperature in Celsius"))
        fahrenheit = temperature * (9/5) + 32
        print(temperature, " degrees Celsius = ", fahrenheit, " degrees Fahrenheit")

    elif option_list == 2:
        print("*****Liters to Gallons Converter*****")
        liters = int(input("Please enter the number of liters"))
        gallons = liters * 0.26417205236
        print(liters, " Liters = ", gallons, " Gallons")

    elif option_list == 3:
        print("*****Number of days to seconds*****")
        days = int(input("Please enter the number of days"))
        seconds = days * 86400
        print('{} days are equal to {} seconds'.format(days, seconds))

    elif option_list == 4:
        print("*****Final price of an item after discount and shipping*****")
        item_price = int(input('Please enter your item price: ').replace(',', '').replace('$', ''))
        location_of_the_user = str(input('Type "West" or "East" to calculate the shipping cost'))

        west_location = "West"
        east_location = "East"
        less_than_fifty = item_price <= 50
        less_than_one_hundred = 50.01 <= item_price <= 100
        less_than_one_hundred_and_fifty = 100.01 <= item_price <= 150
        beyond_one_hundred_and_fifty = item_price

        if location_of_the_user == "West":
            if less_than_fifty:
                print('Your shipping cost is $6.00')
                print('Your grand total is $', item_price + 6)
            elif less_than_one_hundred:
                print('Your shipping cost is $8.00')
                print('Your grand total is $', item_price + 8)
            elif less_than_one_hundred_and_fifty:
                print('Your shipping cost is $10.00')
                print('Your gran total is $', item_price + 10)
            elif beyond_one_hundred_and_fifty:
                print('Congrats your shipping is free!')
                print('Your grand total is: $', item_price)

        if location_of_the_user == "East":
            if less_than_fifty:
                print('Your shipping cost is $3.00')
                print('Your gran total is $', item_price + 3)
            elif less_than_one_hundred:
                print('Your shipping cost is $6.00')
                print('Your grand total is $', item_price + 6)
            elif less_than_one_hundred_and_fifty:
                print('Your shipping cost is $9.00')
                print('Your grand total is $', item_price + 9)
            elif beyond_one_hundred_and_fifty:
                print('Congrats your shipping cost is free!')
                print('Your gran total is $', item_price)
    elif option_list == 5:
        print("Thank", name + ''" for using my program!""\nEnd of the Program")
        break

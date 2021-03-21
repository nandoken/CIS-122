__author__ = 'Fernando Ames'


# This program calculates a final price and the shipping time.
# Input List: item_price, location_of_user
# Output list: discount_price, time_of_shipping, final_price, location_of_user

# Function Real, String get_location_of_user_and_price()
#   Declare Real item_price,
#   Declare String location_of_user
#
#   Display "Please enter the price of the item"
#   Input item_price
#   Display "Please enter the location North America, South America or Central America?"
#   Input location_of_user
#   Return item_price, location_of_user
# End Function

def get_location_of_user_and_price():
    item_price = 0.0
    location_of_user = ""

    item_price = float(input("Please enter the item price: "))
    location_of_user = input("Please enter your location North America, South America or Central America?")
    return item_price, location_of_user


# Function Real calculate_discount_price(Real item_price)
#   Declare Real discount_price
#
#   if item_price >= 100.0 or item_price <= 200.0 then
#       discount_price = 10
#   Else
#       discount_price = 0
#   End if
#   Return discount_price
# End Function

def calculate_discount_price(item_price):
    discount_price = 0.0

    if item_price >= 20.0:
        discount_price = 2
    else:
        discount_price = 0
    return discount_price


# Function Real calculate_total_price(Real item_price, Real discount_price)
#   Declare total_price = 0.0
#
#   total_price = item_price - discount_price
#   Return total_price
# End Function

def calculate_total_price(item_price, discount_price):
    total_price = 0.0

    total_price = item_price - discount_price
    return total_price


# Function Real calculate_time_of_shipping(String location_of_user)
#   Declare Real shipping_time
#
#   if location_of_user == "North America" then
#       shipping_time = 3
#   elif location_of_user == "Central America" then
#       shipping_time = 5
#   elif location_of_user == "South America" then
#       shipping_time = 7
#   else
#       shipping_time = 10
#   End if
#   return shipping_time
# End Function

def calculate_time_of_shipping(location_of_user):
    shipping_time = 0

    if location_of_user == "North America":
        shipping_time = 3
    elif location_of_user == "Central America":
        shipping_time = 5
    elif location_of_user == "South America":
        shipping_time = 7
    else:
        shipping_time = 10
    return shipping_time


# Module output_price_and_shipping (Real discount_price, Real total_price, Real shipping_time, String location_of_user)
#   Display "The location of the user is", location_of_user, "your shipping time is" shipping_time
#   Display "Lucky day you received a -$", discount_price, "discount!"
#   Display "Your total price is:", total_price
# End Module

def output_price_and_shipping(discount_price, total_price, shipping_time, location_of_user):
    print("The location of the user is", location_of_user, "and your shipping time is", shipping_time, "days")
    print("Lucky day! You received a -$", discount_price, "discount!")
    print("Your total price is:$", total_price)


# Module calculate_price_and_shipping()
#   Declare Real item_price
#   Declare String location_of_user
#   Declare Real discount_price
#   Declare Real total_price
#   Declare Real shipping_time
#
#   Set item_price, location_of_user = get_location_of_user_and_price()
#   Set discount_price = calculate_discount_price(item_price)
#   Set total_price = calculate_total_price(item_price, discount_price)
#   Set shipping_time = calculate_time_of_shipping(location_of_user)
#   Call output_price_and_shipping(discount_price, total_price, shipping_time, location_of_user)
# End Module

def calculate_price_and_shipping():
    item_price = 0.0
    location_of_user = ""
    discount_price = 0.0
    total_price = 0.0
    shipping_time = 0

    item_price, location_of_user = get_location_of_user_and_price()
    discount_price = calculate_discount_price(item_price)
    total_price = calculate_total_price(item_price, discount_price)
    shipping_time = calculate_time_of_shipping(location_of_user)
    output_price_and_shipping(discount_price, total_price, shipping_time, location_of_user)


calculate_price_and_shipping()

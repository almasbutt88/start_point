def return_10():
    return 10

#test 2

def add(a, b):
    return a + b

#test 3
def subtract( num1, num2):
    return num1 - num2

#test 4
def multiply( a, b ):
    return a * b

#test 5
def divide(a, b):
    print(a/b)
    return int(a / b)

#test 6
def length_of_string(input):
    return len(input)

#test 7
def join_string(str1, str2):
    return str1 + str2

#test 8
def add_string_as_number(a, b):
    return int(a)+int(b)

#test 9 , 10 and 11
def number_to_full_month_name(a):
    months = {1:"January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
            }
    return months[a]

#test 12, 13 and 14
def number_to_short_month_name(a):
    months = {1:"Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec"
            }
    return months[a]

# test 15
def vol_of_cube(length_of_side):
    return length_of_side * length_of_side * length_of_side

# test 16
def reverse_string(str):
    return str[::-1]

# test 17
def fah_to_cel(fahrenheit):
    return ((fahrenheit-32)*5)/9

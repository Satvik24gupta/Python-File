#Create a program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
def get_integer_input():
    while True:
        try:
            user_input = input("Please enter an integer: ")
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Test the function
try:
    result = get_integer_input()
    print("You entered:", result)
except ValueError as ve:
    print("ValueError occurred:", ve)
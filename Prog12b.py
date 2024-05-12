#Create a program that executes an operation on a list and handles an IndexError exception if the index is out of range.
print()
def list_operation(input_list, index):
    try:
        result = input_list[index]
        # Perform your operation here, for example:
        # result = result * 2
        return result
    except IndexError:
        print("IndexError: Index is out of range.")

# Example list
my_list = [1, 2, 3, 4, 5]
print("list is", my_list)

# Test the function
try:
    index = int(input("Enter an index to access from the list: "))
    print("Result:", list_operation(my_list, index))
except ValueError:
    print("ValueError: Please enter a valid integer index.")
print()
#Create a program to Sort a list of tuples by the second Item
print()
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][1] > lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

tuples = []
while True:
    tpl = input("Enter tuple of two numbers separated by space (e.g., '7 8'). \nPress Enter to stop: ")
    if not tpl:
        break
    data = tuple(map(int, tpl.split()))
    tuples.append(data)

bubble_sort(tuples)

print("Sorted list:", tuples)
print()
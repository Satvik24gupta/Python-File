#Create a program that prompts the user for a list of numbers and then sorts them in ascending order.
print("")
l=[]
n=int(input("Enter size of list: "))
print("Enter Elements of array: ")
 
for i in range(0,n):
    l.append(int(input()))

# print(l)
#Bubble Sort
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
 
print("After sorting")
for i in l:
    print(i)
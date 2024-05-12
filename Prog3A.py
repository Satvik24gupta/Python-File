#Create a program to find factorial of a number using for loop
n=int(input("Enter number to get factorial: "))
fact=1
for i in range(n,1,-1):
    fact*=i
print("Factorial of",n,"is",fact)
print("\n")
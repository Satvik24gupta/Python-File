#Create a program to find factorial of a number using while loop
n=int(input("Enter number to get factorial: "))
fact=1
i=1
while(i<=n):
    fact*=i
    i+=1
print("Factorial of",n,"is",fact)
print("\n")
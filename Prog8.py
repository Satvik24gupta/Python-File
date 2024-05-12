#WAP to fing largest of three numbers
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))

max=n1
if(n2>max):
    max=n2
if(n3>max):
    max=n3

print(max)
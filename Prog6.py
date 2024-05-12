# Create a program that prompts the user for a string and then prints out the string reversed.
print("")
str1=input("Enter String: ")
n=len(str1)
# s=0
# e=n-1
print("Reverse of String:", end=" ")
for i in range(n-1,-1,-1):
    print(str1[i], end="")

print("")
print("")








def AreaOfCircle(r):
    area=3.14*r*r
    return area

if __name__=='__main__':
    print("\n\n")
    r=int(input("Enter radius of Circle: "))
    area=AreaOfCircle(r)
    print("Area of Circle is: ",area)
    print("\n\n")
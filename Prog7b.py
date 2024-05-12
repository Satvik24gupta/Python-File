#Create a program that defines a function to calculate the area of 
#b.) a rectangle based on sides entered by the user.

def AreaOfRectangle(l,b):
    area=l*b
    return area

if __name__=='__main__':
    print("")
    l=int(input("Enter length of Rectangle: "))
    b=int(input("Enter bredth of Rectangle: "))
    area=AreaOfRectangle(l,b)
    print("Area of Rectangle is:",area)
    print("\n\n")


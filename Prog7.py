#Create a program that defines a function to calculate the area of 
#a.) a circle based on the radius entered by the user.

def AreaOfCircle(r):
    area=3.14*r*r
    return area

if __name__=='__main__':
    print("")
    r=int(input("Enter radius of Circle: "))
    area=AreaOfCircle(r)
    print("Area of Circle is: ",area)
    print("\n\n")









#Create a program that defines a class to represent a car and then creates an object of that class with specific attributes

class Car:
    def __init__(self,name,color,wheels):
        self.name=name
        self.color=color
        self.wheels=wheels


# if __name__=='__main__':
Car1=Car("tata","black",4)
Car2=Car("toyoto","white",4)
print(Car1.name,Car1.color,Car1.wheels)
print(Car2.name,Car2.color,Car2.wheels)
#Create a program that prompt the user for their age and test them if they can vote in the upcoming election
age=int(input("Enter your age: "))
if(age>=18):
    print("Congratulations! You are eligible to vote")
else:
    print("Sorry, You are not eligible to vote")
    print("You Will have to wait for",(18-age),"years to vote")
print("\n")

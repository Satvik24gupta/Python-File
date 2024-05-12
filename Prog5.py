print("")
n=int(input("Enter number: "))
sum=0
while(n):
    digit=n%10
    sum+=digit
    n//=10
print(sum)
print("")
print("")
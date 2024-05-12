#Create a program that prints numbers in Fibonacci Series Using Recursion
def Fib(n):
    if(n<=1):
        return n
    return(Fib(n-1)+Fib(n-2))

n=int(input("Enter Value of n: "))
for i in range(n):
    print(Fib(i),end=" ")
# WAP to print fibonacci series of term n and input is given by the user. 
def fibonacci(n):
    a=0
    b=1
    print( f"The Fabonacci Series of Term {n}: ")
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("Enter Number Of Terms Which You Want to Print Fibonacci Series: "))
fibonacci(n)
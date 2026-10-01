# WAP to find the factorial of a number n by using the funtion and input is given by the user.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

n=int(input("Enter Number Which You Want to Find The Factorial:"))
print("The Factorial is:")
factorial(n)
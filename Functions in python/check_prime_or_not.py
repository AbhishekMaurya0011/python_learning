# WAP to check the number is prime or not by using the function and input is given by the user.
def prime_or_not(n):
    count=0
    if n<2:
        print(f"Enter Valid Number")
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print(f"The {n} is a Prime Number ")
    else:
        print(f"The {n} is not a Prime Number")

n=int(input("Enter Number Which You Want to Check the Prime or Not: "))
prime_or_not(n)

        
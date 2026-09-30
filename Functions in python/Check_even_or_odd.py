# WAP to check the even or odd of a number N by the using of function and input is given by user.
def even_odd(n):
    if(n%2==0):
        print(f"The {n} is Even number")
    else:
        print(f"The {n} is Odd Number")
n=int(input("Enter Number Which You Want to Check the Even or Odd: "))

even_odd(n)
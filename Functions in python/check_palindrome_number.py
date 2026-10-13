# WAP to check the number is palindrome or not by using the function and input is given by the user.
def palindrome(n):
    original=n
    rev=0

    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if original==rev:
        print(f"The {original} is Palindrome")
    else:
        print(f"The {original} is Not a Palindrome")

n=int(input("Enter Number to Check the Number is Palindrome or Not: "))
palindrome(n)
# WAP to separate each digit of a number and print it on the new line and input is given by the user.
n=int(input("Enter Number Which You Want to Separate and print the digits :"))
rev=0
while n>0:
    rev=rev*10 + n%10
    n=n//10
print(f"The Reverse Number is: {rev}")

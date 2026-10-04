# WAP to reverse the number by using the function and input is given by the user.
def reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(f"The Reverse Number is {rev}")

n=int(input("Enter number Which You Want to Print Reverse Of a Number: "))
reverse(n)
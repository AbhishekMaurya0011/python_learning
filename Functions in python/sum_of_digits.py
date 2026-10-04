# WAP to find the sum of digits of  number n by using the function and input is given by the user.
def sum_of_digits(n):
    total=0
    while n>0:
        digit=n%10
        total +=digit
        n=n//10
    print(f"The Sum Of Digits is {total}")

n=int(input("Enter Number Which You Want to Sum Of Digits:"))
sum_of_digits(n)
# WAP to check the number n is postive ,negative or zero by using the function and input is given by the user.
def check_number(n):
    if n>0:
        print(f"The {n} is a Positive Numbner")
    elif n<0:
        print(f"The {n} is a Negative Number")
    else:
        print(f"The Number is 0")

n=float(input("Enter Number Which You Want to Check Number is Positive,Negative or Zero: "))
check_number(n)
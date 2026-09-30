# WAP to find the maximum number between of two numbers by using the function and input is given by the user.
def maximum(a,b):
    if a>b:
        print(f"The {a} is Greater than {b}")
    else:
        print(f"The {b} is Greater than {a}")

a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))

maximum(a,b)

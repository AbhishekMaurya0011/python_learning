# WAP to calculate the power of a number and input is given by the user.
def power(a,b):
    answer=0
    answer=a**b
    print(f"The Answer is: {answer}")
a=int(input("Enter Base Number Which You Want to Calculate: "))
b=int(input("Enter Power Number Which you Want To Calculate: "))
power(a,b)
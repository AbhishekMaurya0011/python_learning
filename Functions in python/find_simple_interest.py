# WAP to find the simple interest by using the function and input is given by the user.
def simple_interest(p,r,t):
    print(f"The Simple Interest is {(p*r*t)/100} ")
p=float(input("Enter Principle Amount:"))
r=float(input("Enter Rate:"))
t=float(input("Enetr Time:"))

simple_interest(p,r,t)
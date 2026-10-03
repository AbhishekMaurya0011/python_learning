# WAP to print the multiplication table by using the function and input is given by the user.
def table(n):
    print(f"The Multiplication Table Of {n} is:")
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

n=int(input("Enter Number Which You Want to Print the Multipication Table:"))
table(n)

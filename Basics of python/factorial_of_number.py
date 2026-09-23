# WAP to find the factorial of n number and input is given by the user.
n=int(input("Enter Number Up to Which You Want To Find the Factorial:"))
fact=1

for i in range(1,n+1):
    fact*=i

print(f"The Factorial Of Number is:{fact}")
# WAP to find all the factors of a number and input is given by the user.
n=int(input("Enter Number Which You Want to Find the Factors: "))
fact=0
print(f"The Factors of {n} is:")
for i in range(1,n+1):
    if n%i==0:
     print(i)
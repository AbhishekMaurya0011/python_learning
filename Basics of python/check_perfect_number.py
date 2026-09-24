# WAP to accept a number and check if it a perfect number or not.
n=int(input("Enter Number Which You Want to Check The Number is Perfect or Not:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i

if sum==n:
    print(f"The {n} is Perfect Number")
else:
    print(f"The {n} is Not Perfect number")
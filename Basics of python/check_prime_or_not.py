# WAP to check Wether the number is prime or not.
n=int(input("Enter Number Which You Want to Check the Number is Prime or Not:"))
count=0
for i in range(1,n+1):
    if n%i==0:
     count+=1
if count==2:
   print(f" {n} is prime Number")
else:
   print(f" {n} is Not Prime number")
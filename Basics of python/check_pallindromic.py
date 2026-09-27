#WAP to accept a number and check if it is a pallindromic number or Not and input is given by the user. 
n=int(input("Enter number Which You Want to Check Pallindromic Number:"))
copy=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if copy==rev:
    print(f"The {copy} is a Pallindromic Number")
else:
    print(f"The {copy} is Not a Pallindromic Number")
    

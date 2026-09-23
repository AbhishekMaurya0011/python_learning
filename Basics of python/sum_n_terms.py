# WAP to find the sum of n number of terms and input is given by the user.
n=int(input("Enter Number Up to Which You Want to Find the Sum: "))
sum=0
for i in range(1,n+1):
    sum+=i

print(f"The Sum Of N Terms is:{sum}")
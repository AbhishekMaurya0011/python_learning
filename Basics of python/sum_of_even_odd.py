# WAP to find the sum of all even & odd numbers in a range separately and input is given by the user.
n=int(input("Enter Number Up to Which You Want to Find the Sum: "))
odd=0
even=0
for i in range(1,n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i

print(f"The sum Of Even Number is:{even}")
print(f"The Sum Of Odd Number is:{odd}")
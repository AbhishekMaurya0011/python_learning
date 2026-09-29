#WAP to print the odd numbers up to n number and input is given by the user .
n=int(input("Enter the Number Up to Which You Want to print the Odd Number: "))
print("The Odd Number is:")
for i in range(1,n+1):
    if(i%2!=0):
        print(i)

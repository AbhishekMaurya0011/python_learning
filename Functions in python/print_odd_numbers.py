# WAP to print the odd numbers by using the function up to number n and input is given by the user.
def print_odd_numbers(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)

n=int(input("Enter Number Up to Which You Want to Print Odd Numbers:"))
print("The Odd Number is:")
print_odd_numbers(n)
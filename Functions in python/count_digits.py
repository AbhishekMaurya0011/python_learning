# WAP to count digits of a number byb using the function and input is given by the user.
def count_digits(n):
    count=0

    while n>0:
        count+=1
        n=n//10
    print(f"The Count Of Digits is: {count}")
n=int(input("Enter Number Which You Want Count Digits Of Numbers: "))
count_digits(n)
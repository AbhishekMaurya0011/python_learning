# WAP to count a digits of a number by using the function and input is given by the user.
def count_of_digit(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    print(f"The Count of Digits is {count}")
n=int(input("Enter Number Which You Want to Count of Ditits: "))
count_of_digit(n)

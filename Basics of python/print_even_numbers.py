#WAP to print the even numbers up to n number and the input is given by the user.
n=int(input("Enter the Number Up to Which You Want to Print The even Numbers:"))
print("The Even number is:")
for i in range(1,n+1,):
    if(i%2==0):
        print (i)
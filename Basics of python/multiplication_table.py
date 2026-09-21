# WAP to print the multiplication table and number is given by the user.
n=int(input("Enter Your Number Which Table You Want to Print? "))
print ("The Table is:")
for i in range(n,(n*10)+1,n):
    print(i)
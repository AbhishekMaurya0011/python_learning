#Accept name and age from the user .check if the user is valid voter or not.
a=(input ("Enter Your First Name:"))
b=(input ("Enter Your Last Name:"))
c=int(input("Enter Your Age:"))

print(a+" "+b)
if(c>=18):
    print( a+" "+b+ " you can vote")
else :
    print(a+" "+b+"you can not vote")

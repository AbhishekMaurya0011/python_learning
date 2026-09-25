# WAP to check string is pallindrome or not and input is given by the user.
a=str(input("Enter the Word Which you Want to Check the Word is pallindrome Or Not: "))
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]

if(b==a):
    print(f"The {a} is Pallindrome")
else:
    print(f"The {a} is Not pallindrome")
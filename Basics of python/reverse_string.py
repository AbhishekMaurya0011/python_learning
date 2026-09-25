# WAP to reverse a string without using in build functions and input is given by user.
a=str(input("Enter String Which You Want to Reverse the String: "))
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]

print(f"The Reverse String is: {b}")    
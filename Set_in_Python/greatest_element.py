# WAP to find the greatest element in a set and input is given by the user.
s=set(map(int,input("Enter Elements ina Set:").split()))
print("The Set is: ",s)
s=list(s)
largest=s[0]
for i in range(len(s)):
    if s[i]>largest:
        largest=s[i]
print("The Largest Element in a Set is: ",largest)
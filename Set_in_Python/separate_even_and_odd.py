# WAP to separate even and odd elements in a different set and input is given by user.
s=set(map(int,input("Enter Elements are in a Set: ").split()))
print("The Set is: ",s)
even=set()
odd=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("The Even Elements are: ",even)
print("The Odd Elements are: ",odd)

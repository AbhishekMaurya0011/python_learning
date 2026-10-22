# WAP to find the maximum and minimum elements in a set and input is given by the user.
s=set(map(int,input("Enter Elements in a Set: ").split()))
print("The Set is: ",s)
if s:
    print("The Maximum Element is: ",max(s))
else:
    print("The Set is Empty!")

if s:
    print("The Minimum Element is: ",min(s))
else:
    print("The Set is Empty!")
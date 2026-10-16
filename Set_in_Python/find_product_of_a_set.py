# WAP to find the product of elements in a set and input is given by the user.
s=set(map(int,input("Enter Elements in a Set: ").split()))
print("The Set is: ",s)
product=1
for i in s:
    product*=i
print("The Product of a Elements in a Set is :",product)
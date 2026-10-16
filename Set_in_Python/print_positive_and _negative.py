# WAP to print the positive and negative elements in a set and the input is given by the user
s=set(map(int,input("Enter Elements in the Set: ").split()))
print("The Set is: ",s)
print("\n")
print("The Psitive Elements in the Set is: ")
for i in s:
    if i>=0:
        print(i)
print("\n")
print("The Negative Elements in the set is: ")
for i in s:
    if i<0:
        print(i)
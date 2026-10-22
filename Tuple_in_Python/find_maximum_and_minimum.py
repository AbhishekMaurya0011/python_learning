# WAP to find the maximum and minimum elements in a tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Tuple : "))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in a Tuple: "))
    t+=(value,)
print("The Tuple is:",t)
if t:
    print("The Maximum Element is:",max(t))
if t:
    print("The Minimum Element is:",min(t))
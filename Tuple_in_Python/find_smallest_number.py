# WAP to find the smallest element in the tuple and input is given by the user.
n=(int(input("Enter How Many Elements are Adding in the Tuple: ")))
t=()

for i in range(n):
    value=(int(input(f"Enter Element {i+1} in the tuple: ")))
    t+=(value,)
print("The Tuple is:",t)
smallest=t[0]
for i in t:
    if i<smallest:
        smallest=i
print("The Smallest Element in the Tuple is:  ",smallest)
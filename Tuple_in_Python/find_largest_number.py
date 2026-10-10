# WAP to find the largest element in the tuple and input is given by the user.
n=(int(input("Enter How Many Elements are Adding in the Tuple: ")))
t=()

for i in range(n):
    value=(int(input(f"Enter Element {i+1} in the tuple: ")))
    t+=(value,)
print("The Tuple is:",t)
largest=t[0]
for i in t:
    if i>largest:
        largest=i
print("The Largest Element in the Tuple is:  ",largest)
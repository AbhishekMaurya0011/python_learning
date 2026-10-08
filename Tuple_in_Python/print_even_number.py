# WAP to print even elements from tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple: "))
    t+=(value,)

print("The Tuple is ",t)
print("The Even Elements in the Tuple is: ")
for i in t:
    if i%2==0:
        print(i)
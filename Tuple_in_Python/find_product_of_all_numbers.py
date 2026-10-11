# WAP to find the product of the tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()
product=1
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple: "))
    t+=(value,)
print("The Tuple is: ",t)
for i in t:
    product*=i
print("The Product Of Tuple is: ",product)
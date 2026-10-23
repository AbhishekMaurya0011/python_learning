# WAP to create a tuple of squares and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Tuple : "))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in a Tuple:"))
    t+=(value,)
print("The Tuple is: ",t)
square=()
for i in t:
    square+=(i*i,)
print("The Square Of a Tuple is: ",square)
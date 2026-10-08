# WAP to convert a tuple into a list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()

for i in range(n):
    value=int(input(f"Enter {i+1} Elements in the Tuple: "))
    t=t+(value,)
l=list(t)
print("The Tuple is ",t)
print("The List is ",l)
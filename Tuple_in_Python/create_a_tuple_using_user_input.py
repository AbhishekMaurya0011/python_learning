# WAP create a tuple using user input.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()

for i in range(n):
    value=int(input(f"Enter {i+1} Elements in the Tuple: "))
    t=t+(value,)
print("The Tuple is: ",t)
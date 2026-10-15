# WAP to check whether a tuple is empty or not and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List:"))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in a Tuple:"))
    t+=(value,)
print("The Tuple is: ",t)
if len(t)==0:
        print("The Tuple is Empty.")
else:
        print("The Tuple is Not Empty.")
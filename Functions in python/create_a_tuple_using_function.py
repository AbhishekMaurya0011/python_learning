# WAP to create a tuple using function and input is given by the user.
def create_tuple(n):
    

    print("The Tuple is: ",t)
    print("The Length Of a Tuple is: ",len(t))
    print("The Maximum Element in a Tuple is: ",max(t))
    print("The Minimum Element in a Tuple is: ",min(t))
    print("The Sum Of a Tuple is: ",sum(t))

n=int(input("Enter How Many Elements are Adding in a Tuple : "))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in a Tuple:"))
    t+=(value,)

if n>0:
    create_tuple(t)
else:
    print("Please Enter at Least One Element")

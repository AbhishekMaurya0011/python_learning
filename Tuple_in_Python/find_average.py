#WAP to find the average of tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple: "))
    t=t+(value,)
print("The Tuple is ",t)
average=sum(t)/len(t)
print("The Average Of a Tpule is: " ,average)
# WAP to find the elements are not divisible by the n in a tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Tuple: "))
t=()
for i in range(n):
    value=(int(input(f"Enter Element {i+1} in a Tuple: ")))
    t+=(value,)
print("The Tuple is: ",t)
n=int(input("Enter Number Which You Want To Check Elements are Divisible in a Tuple: "))
result=()
for i in t:
    if i%n!=0:
       result+=(i,)
print(f"The Elements Which are Not Divisible by {n} in a Tuple are:  ",result)
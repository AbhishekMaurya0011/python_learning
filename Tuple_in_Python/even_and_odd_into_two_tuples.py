# WAP to separate the even and odd elements into two different tuples and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} i the Tuple: "))
    t+=(value,)
print("The Tuple is: ",t)
even=()
odd=()
for i in t:
    if i%2==0:
        even+=(i,)
    else:
        odd+=(i,)
print("The Even Tuple is: ",even)
print("The Odd Tuple is: ",odd)
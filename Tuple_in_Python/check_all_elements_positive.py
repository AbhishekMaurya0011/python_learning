# WAP to check the all the elements of a tuple is positive or not and input is given by the user. 
n=int(input("Enter How Many Elements are Adding in the Tuple :"))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple :"))
    t+=(value,)
print("The tuple is:",t)
positive=True
for i in t:
    if i<=0:
        positive=False
if positive:
    print(" All The Elements are Positive in the Tuple ")
else:
    print("All The Elements are Not Positive in the Tuple")

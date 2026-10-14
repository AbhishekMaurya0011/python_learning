# WAP to separate the positive and negative elements in  two different tuples and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple :"))
t=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple :"))
    t+=(value,)
print("The Tuple is :",t)
positive=()
negative=()
for i in t:
    if i>=0:
        positive+=(i,)
    else:
        negative+=(i,)
print("The Positive Elements in the Tuple is :",positive)
print("The Negative Elements in the Tuple is :",negative)
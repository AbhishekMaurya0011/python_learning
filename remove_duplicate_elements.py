# WAP to remove the duplicate elements in a tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Tuple: "))
t=[]
for i in range(n):
    value=(int(input(f"Enter Element {i+1} in a Tuple: ")))
    t+=(value,)
print("The List is: ",t)
unique=()
for i in t:
    if i not in unique:
        unique+=(i,)
print("The Tuple is Without Duplicates value: ",unique)
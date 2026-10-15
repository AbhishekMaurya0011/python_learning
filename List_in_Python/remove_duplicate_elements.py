# WAP to remove the duplicate elements in a list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a List:"))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in a List:")))
print("The List is: ",l)
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print("The List is Without Duplicates value: ",unique)

# WAP to take list elements from the user and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a List: "))
l=[]
for i in  range(n):
    l.append(int(input(f"Enter Element {i+1} in a List: ")))
print("The List is: ",l)
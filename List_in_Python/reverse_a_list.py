# WAP to reverse a list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in the List: ")))
print("The List is: ",l)
l.reverse()
print("The Reverse List is: ",l)
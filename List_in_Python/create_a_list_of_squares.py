# WAP to create a list of squares and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in a List: ")))
print("The List is:",l)
square=[]
for i in l:
    square.append(i**2)

print("The Square Of a List is: ",square)
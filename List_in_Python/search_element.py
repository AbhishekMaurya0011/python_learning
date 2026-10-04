# WAP to search the element in a list and the input is given by the user.
l=[]
n=int(input("Enetr How Many Elements are Yor Adding in the List: "))
print("\n")
for i in range(n):
    l.append(int(input(f"Enter {i+1} Number Which you Want to Adding in the List: ")))
print("\n")

x=int(input("Enter Number Which You Want to Search in the List: "))
print("\n")
if x in l:
    print(f"The {x} is Found in the List")
else:
    print(f"The {x} is Not Found in the List")
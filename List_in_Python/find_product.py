# WAP to find the product of a list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List : "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in the List: ")))
print("The List is: ",l)
product=1
for i in l:
    product*=i
print("The Product Of List is: ",product)
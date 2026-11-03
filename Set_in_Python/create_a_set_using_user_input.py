# WAP to create a set using user input.
s=set()
n=int(input("Enter How Many Elements are Adding in a Set: "))
for i in range(n):
    x =int(input(f"Enter Element {i+1} in a Set: "))
    s.add(x)
print("The Set is: ",s)
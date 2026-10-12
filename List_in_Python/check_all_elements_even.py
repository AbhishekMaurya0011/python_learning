# WAP to check all the elements are in the list is even or not and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in the List: ")))
print("The List is: ",l)
even=True
for i in l:
    if i%2!=0:
        even=False
        break
if even:
    print("All Elements are in the List is Even Elements.")
else:
    print("All Elements are in the List is Not Even Elements.")

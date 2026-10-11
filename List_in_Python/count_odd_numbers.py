# WAP to count the odd elements in the list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in the list: ")))
print("The List is: ",l)
count=0
for i in l:
    if i%2!=0:
        count+=1
print("The Odd Elements in the List is: ",count)

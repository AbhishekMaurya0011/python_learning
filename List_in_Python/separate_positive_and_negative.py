# WAP to separate the positive and negative elements in the two different list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in the List: ")))
print("The List is: ",l)
positive=[]
negative=[]
for i in l:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)
print("The Positve Elements are in the List is: ",positive)
print("The Negative Elements are in the List is: ",negative)
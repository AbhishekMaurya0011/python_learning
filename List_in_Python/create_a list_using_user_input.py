# WAP to create a list using user input.
l=[]
n=int(input("Enter How Many Element are You Adding in List:"))

for i in range(n):
    l.append(int(input(f"Enter Element {i+1} Which You Want to Add in a List: ")))
print("The List Elements are:")
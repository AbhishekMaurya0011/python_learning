# WAP to find the maximum value in a dictionary and input is given by the user.
n=int(input("Enter How many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1} : ")
    value=int(input(f"Enter Value Element {i+1} : "))
    d[key]=value
print("The Dictionary is: ",d)
print("The Maximum Value in a Dictionary is: ",max(d.values()))
print("The Minimum Value in a Dictionary is: ",min(d.values()))
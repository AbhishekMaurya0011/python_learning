# WAP to create a dictionary and square its values and input is given by the user.
n=int(input("Enter How many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=int(input(f"Enter Key Element {i+1} : "))
    value=int(input(f"Enter Value Element {i+1} : "))
    d[key]=value
print("The Dictionary is: ",d)
for i in d:
    d[i]=d[i]*d[i]
print("The Square Of a Dictionary Value is:",d)
# WAP to find average of a value of a dictionary and input is given by the user.
n=int(input("Enter How many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1} : ")
    value=int(input(f"Enter Value Element {i+1} : "))
    d[key]=value
print("The Dictionary is: ",d)
average=sum(d.values())/len(d)
print("The Average Of a Dictonary is: ",average)
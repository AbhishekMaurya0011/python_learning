# WAP to find the sum of dictionary values and input is given by the user.
n=int(input("Enter How Many Elements in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1} :")
    value=int(input(f"Enter Value Element {i+1} :"))
    d[key]=value
print("The Dictionary is: ",d)
print("The Sum of Dictionary Values is: ",sum(d.values()))

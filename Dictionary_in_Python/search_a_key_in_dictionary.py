# WAP to search a key element in a dictionary and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1}: ")
    value=input(f"Enter Value Element {i+1}: ")
    d[key]=value

search=(input("Enter Key Element to Search: "))
if search in d:
    print("The key Element is Found.")
    print("The Value is:", d[search])
else:
    print("Key Not Found")

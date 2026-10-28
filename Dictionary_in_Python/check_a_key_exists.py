# WAP to check whether a key exists or not in a dictionary and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1}: ")
    value=input(f"Enter Value Element {i+1}: ")
    d[key]=value
print("The Dictionary is: ",d)

for i in d:
    key= input("\n Enter Key Element to Search :")
    if key in d:
        print(" The Key Element is Exist")
        break
    else:
        print(" The Key Element Does Not Exist")
        break
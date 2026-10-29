# WAP to check whether a Value exists or not in a dictionary and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1}: ")
    value=input(f"Enter Value Element {i+1}: ")
    d[key]=value
print("The Dictionary is: ",d)

for i in d:
    value= input("\n Enter Value Element to Search :")
    if value in d:
        print(" The Value Element is Exist")
        break
    else:
        print(" The Value Element Does Not Exist")
        break
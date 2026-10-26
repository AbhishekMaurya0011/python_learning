# WAP to swap dictionary keys and values and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a Dictionary: "))
d={}
for i in range(n):
    key=input(f"Enter Key Element {i+1}: ")
    value=input(f"Enter Value Element {i+1}: ")
    d[key]=value
print("The Dictionary is: ",d)
result={}
for key,value in d.items():
    result[value]=key
print("The Dictionary After Swapping is:",result)
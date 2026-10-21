# WAP to create a student marks dictionary and input is given by the user.
n=int(input("Enter How Many Students are Adding in a Dictionary: "))
d={}
for i in range(n):
    while True:
        name=(input(f"Enter Key Element {i+1} : "))
        if name.isalpha():
            break
        else:
            print("Please Enter Characters Only!")
    marks=int(input(f"Enter Marks Element {i+1} : "))
    d[name]=marks
print("The Dictionary is:",d)
for name,marks in d.items():
    print(name," Marks Scored: ",marks)
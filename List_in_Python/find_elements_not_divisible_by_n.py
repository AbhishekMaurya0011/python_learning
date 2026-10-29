# WAP to find the elements are not divisible by the n in a list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in a List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in a List: ")))
print("The Set is: ",l)
n=int(input("Enter Number Which You Want To Check Elements are Divisible in a List: "))
result=[]
for i in l:
    if i%n!=0:
       result.append(i)
print(f"The Elements Which are Not Divisible by {n} in a List are:  ",result)
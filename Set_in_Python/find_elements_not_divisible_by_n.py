# WAP to find the elements are not divisible by the n in a set and input is given by the user.
s=set(map(int,input("Enter Elements in a Set: ").split()))
print("The Set is: ",s)
n=int(input("Enter Number Which You Want To Check Elements are Not Divisible in a Set: "))
result=[]
for i in s:
    if i%n!=0:
       result.append(i)
print(f"The Elements Which are Not Divisible by {n} in a Set are:  ",result)
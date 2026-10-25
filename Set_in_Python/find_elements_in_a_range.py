# WAP to find the numbers within a given range and input is given by the user.
s=set(map(int,input("Enter Elements in a Set: ").split()))
print("The Set is: ",s)
low=int(input("Enter Lower Limit: "))
high=int(input("Enter High Limit: "))
result=[]
for i in s:
    if low<=i<=high:
        result.append(i)
print(f"The Elements Between {low} and {high} is:",result)
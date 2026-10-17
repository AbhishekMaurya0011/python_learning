# WAP to find the mean of a set and input is given by the user.
s=set(map(int,input("Enter Elements in a Set: ").split()))
print("The Set is: ",s)
total_sum=0
for i in s:
    total_sum+=i
print("The Mean Of a set is: ",total_sum/len(s))
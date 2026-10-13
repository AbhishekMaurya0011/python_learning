# WAP to Sum of even and odd elements from a set and input is given by the user.
s=set(map(int,input("Enter Elements in the set:").split()))
print("The Set is:",s)
sum_even=0
sum_odd=0
for i in s:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("The Sum Of Even Elements are in the set is:",sum_even)
print("The Sum Of Odd Elements are in the set is:",sum_odd)
# WAP to count numbers of even and odd elements from a set and input is given by the user.
s=set(map(int,input("Enter Elements in the set:").split()))
print("The Set is:",s)
count_even=0
count_odd=0
for i in s:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("The Count Of Even Elements are in the set is:",count_even)
print("The Count Of Odd Elements are in the set is:",count_odd)

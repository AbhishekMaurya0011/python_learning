# WAP to count the positive and negative elements in a set and input is given by the user.
s=set(map(int,input("Enter Elements in the Set: ").split()))
print("The Set is: ",s)
count_positive=0
count_negative=0
for i in s:
    if i>=0:
        count_positive+=1
    else:
        count_negative+=1
print("The Count Of Positive Elements in a Set is : ",count_positive)
print("The Count Of Negative Elements in a Set is : ",count_negative)

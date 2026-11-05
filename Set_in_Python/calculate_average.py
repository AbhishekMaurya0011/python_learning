# WAP to calulate average and input is given by the user.
s=set(map(int,input("Enter Elements in a Set: ").split()))
if s:
    print("The Average Of a Set is: ",sum(s)/len(s))
else:
    print("The Set is Empty")
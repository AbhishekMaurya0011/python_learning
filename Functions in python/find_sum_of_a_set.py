# WAP to find the sum of a Set by using the function and input is given by the user.
def set_sum(s):
    sum=0
    print("The Set is: ",s)
    for i in s:
        sum+=i
    print("The Sum Of a Set is :",sum)
s=set(map(int,input("Enter Elements in a Set: ").split()))
set_sum(s)
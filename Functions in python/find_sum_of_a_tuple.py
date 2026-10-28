# WAP to find the sum of a tuple by using the function and input is given by the user.
def tuple_sum(t):
    sum=0
    print("The Tuple is: ",t)
    for i in t:
        sum+=i
    print("The Sum Of a Tuple is :",sum)

n=int(input("Enter How Many Elements are Adding in a Tuple: "))
t=()
for i in range(n):
    value=(int(input(f"Enter Element {i+1} in a Tuple: ")))
    t+=(value,)
tuple_sum(t)
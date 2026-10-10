# WAP to find the sum of all even elements in the tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the tuple: "))
t=()
sum_even=0
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple: "))
    t+=(value,)
print("The Tuple is: ",t)
for i in t:
    if i%2==0:
        sum_even+=i
print("The Sum Of All Even Elements in the Tuple is: ",sum_even)

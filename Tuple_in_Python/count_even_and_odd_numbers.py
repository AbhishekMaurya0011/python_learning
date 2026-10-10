# WAP to count the even and odd number of elements in the tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the Tuple: "))
t=()
even=0
odd=0
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple: "))
    t=t+(value,)
print("The Tuple is: ",t)

for i in t:
   if i%2==0:
    even+=1
   else:
      odd+=1

print("The Number Of Even Elements in Tuple is: ",even)
print("The Number Of Odd Elements in Tuple is: ",odd)
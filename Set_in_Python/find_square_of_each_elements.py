# WAP to find the square of each elements in a set and input is given by the user.
s=set(map(int,input("Enter Elements in a set: ").split()))
print("The Set is: ",s)
squares=set()
for i in s:
    squares.add(i*i)
print("The Square of Each Elements is: ",squares)
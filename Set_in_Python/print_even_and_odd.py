# WAP to print the even and odd elements from a set and input is given by the user.
s=set(map(int,input(f"Enter Element in the set :").split()))
print("The Set is :",s)
print("The Even Elements in the set is:")
for i in s:
    if i%2==0:
        print(i)
print("The Odd Elements in the set is:")
for i in s:
    if i%2!=0:
        print(i)
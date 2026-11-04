# WAP to find prime numbers in a tuple and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the tuple: "))
t=()
prime=()
for i in range(n):
    value=int(input(f"Enter Element {i+1} in the Tuple: "))
    t+=(value,)
print("The Tuple is: ",t)

for i in t:
    if i>1:
        flag=True

        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag==True:
            prime+=(i,)
print("The Prime Numbers in a Tuple are:",prime)

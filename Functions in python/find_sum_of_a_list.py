# WAP to find the sum of a list by using the function and input is given by the user.
def list_sum(l):
    sum=0
    print("The List is: ",l)
    for i in l:
        sum+=i
    print("The Sum Of a List is :",sum)

n=int(input("Enter How Many Elements are Adding in a List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in a List: ")))
list_sum(l)

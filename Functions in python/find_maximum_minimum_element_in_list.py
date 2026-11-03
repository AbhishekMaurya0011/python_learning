# WAP to find the maximum and minimum element in a list and input is given by the user.
def calculate(a):
    maximum = a[0]
    minimum = a[0]

    for i in a:
        if i>maximum:
            maximum=i

        if i<minimum:
            minimum=i
    print("The Maximum Element in a List is: ",maximum)
    print("The Minimum Element in a List is: ",minimum)

n=int(input("Enter How Many Elements are Adding in a List: "))
a=[]
for i in range(n):
    a.append(int(input(f"Enter Element {i+1} in a List: ")))

calculate(a)
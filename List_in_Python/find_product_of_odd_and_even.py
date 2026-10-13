# WAP to find the product of even and odd elements in the list and input is given by the user.
n=int(input("Enter How Many Elements are Adding in the List: "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element {i+1} in the List: ")))
print("The List is: ",l)
product_positive=1
product_negative=1
for i in l:
    if i%2==0:
        product_positive*=i
    else:
        product_negative*=i
print("The Product Of Even Elements is: ",product_positive)
print("The Product Of Odd Elements is: ",product_negative)
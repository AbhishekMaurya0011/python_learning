# WAP to print the even and odd numbers and the element is enter by the user in the list.
l=[]
n=int(input("Enter How Many Elemnts are Added in Lists: "))
print("\n")
for i in range(n):
    l.append(int(input(F"Enter Number {i+1} Which You Want to Add in the list : ")))
print("\n")

print("The Even numbers are: ")
for i in l:
    if i%2==0:
        print(i)
print("\n")
print("The Odd Numbers are: ")
for i in l:
    if i%2!=0:
        print(i)
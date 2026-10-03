# WAP to print the even and odd numbers separately of a given list.
l=[34,80,59,79,65,45,46,76,89,56,45,20]
print("The Even numbers are: ")
for i in l:
    if i%2==0:
        print(i)
print("\n")
print("The Odd Numbers are:")
for i in l:
    if i%2!=0:
        print(i)
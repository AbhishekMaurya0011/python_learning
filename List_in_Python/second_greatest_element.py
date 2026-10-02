#WAP to find the second greatest element of a given list.
l=[23,65,54,76,67,85,54,43,89,43,78]
greatest=l[0]
second_greatest=l[0]
for i in l:
    if i>greatest:
        second_greatest=greatest
        greatest=i
    elif i>second_greatest:
        second_greatest=i
print(f"The Second Greatest Element is:{second_greatest}")
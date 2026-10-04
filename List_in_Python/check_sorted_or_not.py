# WAP to check if given list is sorted or not.
l=[66,67,68,69,71,78,88]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("The List is Not Sorted")
        break
else:
    print(f"The List: {l}  is Sorted")
l=[]
n=int(input("Enter How Many Elements are Adding in the List: "))
sum=0

for i in range(n):
    l.append(int(input(f"Enter {i+1} Number Which You Want to Adding in the List: ")))

for i in l:
    sum+=i
print(f" The Sum Of The Elements is: {sum}")


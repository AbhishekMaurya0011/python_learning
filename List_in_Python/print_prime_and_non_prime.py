# WAP to print the prime and non prime Elements separately and elements of list is given by the user. 
l=[]
n=int(input("Enter How Many Element are You Adding in List:"))

for i in range(n):
    l.append(int(input(f"Enter Element {i+1} Which You Want to Add in a List: ")))
print("The Prime Elements are:")
for num in l:
    if num>1:
        count=0
        for i in range(2,num):
            if num%i==0:
             count+=1
        if count==0:
            print(num)
print("\n")
print("The Non Prime Elements are:")

for num in l:
    if num<=1:
        print(num)
    else:
        count=0
        for i in range(2,num):
            if num%i==0:
                count+=1
        if count!=0:
                print(num)

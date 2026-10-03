# WAP to print the prime and non prime numbers separately and elements of list is given by the user. 
l=[]
n=int(input("Enter How Many Element are You Adding in List:"))

for i in range(n):
    l.append(int(input(f"Enter {i+1} Number Which You Want to Add in List: ")))
print("The Prime Numbers are:")
for num in l:
    if num>1:
        count=0
        for i in range(2,num):
            if num%i==0:
             count+=1
        if count==0:
            print(num)
print("\n")
print("The Non Prime Numbers are:")

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
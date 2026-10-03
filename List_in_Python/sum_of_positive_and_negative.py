# WAP to calculate the sum of positive and negative elements in the list separately and input is given by the user.
l=[]
n=int(input("Enter How Many Element Yow Want to Adding in the List: "))
print("\n")
for i in range(n):
    l.append(int(input(f"Enter {i+1} Number Which You Want to Adding in the List: ")))
print("\n")
positive=0
negative=0
for x in l:
    if x>0:
       positive+=x
    else:
        negative+=x
print("The Sum Of Positive Elements is:" ,positive)
print("The Sum Of Negative Elements is:" ,negative)
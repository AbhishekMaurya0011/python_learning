# WAP to find the lcm of two numbers by using the function and input is given by the user.
def lcm(a,b):
    x,y=abs(a),abs(b)

    if x==0 or y==0:
        print("The LCM is: 0")
        return
    while y!=0:
        x,y=y,x%y
    result=abs(a*b)//x
    print("The LCM is:",result)

a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))
lcm(a,b)
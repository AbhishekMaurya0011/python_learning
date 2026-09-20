#Accept a year and check if it a leap year or not .
year=int(input("Enter Year:"))
if(year%400==0):
    print(year,"is a Leap Year")
elif(year%100==0):
    print(year,"is not a Leap Year")
elif(year%4==0):
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")
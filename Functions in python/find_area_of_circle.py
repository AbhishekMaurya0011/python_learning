# WAP to find the area of a circle by using the function and input is given bythe user.
def area_of_circle(r):
    area=3.14*r*r
    print(f"The Area Of a circle is {area} Square Unit")

r=float(input("Enter Radius Of a circle Which You Want to Find Area Of Circle:"))
area_of_circle(r)
# WAP to check the year is leap year or not by using the function and input is given by the user.
def check_leap_year(year):
    if year%400==0 or (year%4==0 and year%100 !=0):
        print(f"The {year} is a Leap Year")
    else:
        print(f"The {year} is not a leap year")
year=int(input("Enetr year Which You Want to Check The Year is Leap Year Or Not:"))
check_leap_year(year)
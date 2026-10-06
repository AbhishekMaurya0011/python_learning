#  WAP to convert the fahrenheit temprature into the celsius temprature and input is given by the user.
def fahrenheit_to_celsius(f):
    return (f-32)*5/9
f=float(input("Enter Fahrenheit Temprature Which You Want to Convert in Celsius Temprature : "))
print("The Celsius Temprature is ",fahrenheit_to_celsius(f),"degrees celsius")
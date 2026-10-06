# WAP to convert the celsius temprature into the fahrenheit temprature and input is given by the user.
def celsius_to_fahrenheit(c):
    return(c*9/5) + 32
c=float(input(f"Enter Celsius Temprature Which You Want to Convert in Fahrenheit: "))
print("The Fahrenheit Temprature is",celsius_to_fahrenheit(c),"degrees fahrenheit")
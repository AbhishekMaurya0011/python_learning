# take input of temperature in celsius
temp= int(input("Enter Temperature:"))
if(temp<0):
    print("Freezing cold")
elif(temp>0 and temp<=10):
    print("Very Cold")
elif(temp>10 and temp<=20):
    print("cold")
elif(temp>20 and temp<=30):
    print("Pleasent")
elif(temp>30 and temp<=40):
    print("Hot")
else:
    print("Very Hot")

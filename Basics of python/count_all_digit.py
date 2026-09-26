# WAP to count all letters,digits and special symbols from a string and string is given by the user.
a=str(input("Enter String Which You Want to Count All Digit:"))
char=0
digits=0
symbol=0

for i in a:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        char+=1
    else:
        symbol+=1

print(f"The Digits are:{digits}")
print(f"The Chars are:{char}")
print(f"The Symbols are:{symbol}")
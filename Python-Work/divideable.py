print("I can tell you if a number is dividable by 2 or 3 or both\n")

x  = int(input("Input number: "))

if (x / 2).is_integer():
    print(f"{x} Can be divided by 2.")
if (x / 3).is_integer():
    print(f"{x} Can be divided by 3.")
else:
    print(f"{x} Can't be divided by 2 or 3.")
            


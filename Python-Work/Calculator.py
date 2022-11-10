import math
import random

temp = ""

def calc():

    c = ""

    print("Számológép:")
    
    print("")

    print("Választható műveletek:")
    print("+")
    print("-")
    print("/")
    print("*")
    print("abs - (abszolút érték)")
    print("opp - (ellentét)")
    print("random - (véletlenszerű szám a megadott határon belül)")
    print("average - (megmondja bármely számok átlagát)")
    print("even - (páros-e a megadott szám)")
    print("sq - (négyzetre emelés)")
    print("LCM - (legkisebb közös többszörös)")
    print("GCD - (legnagyobb közös osztó)")
    print("between(2) - (két szám közötti értékek)")
    
    print("")

    print("Írd be a művelet jelét a számolás elíndításához.")
    
    print("")

    n = str(input("Művelet: "))

    if n == "+":
    
        def add(a,b):
            x = a + b
            return x

        a = float(input("1. szám: "))
        b = float(input("2. szám: "))
        print(add(a,b)) 
            

    if n == "-":
            
        def sub(a,b):
            x = a - b
            return x

        a = float(input("1. szám: "))
        b = float(input("2. szám: "))
        print(sub(a,b))

    if n == "*":
            
        def mul(a,b):
            x = a * b
            return x

        a = float(input("1. szám: "))
        b = float(input("2. szám: "))
        print(mul(a,b))

    if n == "/":
            
        def div(a,b):
            x = a / b
            return x

        a = float(input("1. szám: "))
        b = float(input("2. szám: "))
        print(div(a,b))

    if n == "abs":
        def absolute(a):
            x = abs(a)
            return x
        
        a = float(input("Szám: "))
        print(absolute(a))

    if n == "ell":

        def ell(a):
            x = a - (2*a)
            return x

        a = float(input("Szám: "))
        print(ell(a))

    if n == "random":
        
        def rand(a,b):
            x = random.randrange(a, b)
            return x

        a = float(input("1. szám: "))
        b = float(input("2. szám: "))
        print(rand(a,b))

    if n == "average":
        def avg(list):
            return sum(list) / len(list)
  
        list = []

        nums = int(input("Hány számot akarsz átlagolni? "))

        for i in range(0, nums):
            ele = int(input())


        list.append(ele)

        print(avg(list))

    if n == "sq":
            
        def sq(a):
            x = a * a
            return x

        a = float(input("Szám: "))
        print(sq(a))

    if n == "even":
        a = float(input("Szám: "))

        if (a % 2) == 0:
            print(a, ",páros")
        else:
            print(a, ", páratlan")

    if n == "GCD":

        def gcd(a,b):
            return math.gcd(a,b)

        a = int(input("1. szám: "))
        b = int(input("2. szám: "))
        print(gcd(a,b))            
    
    if n == "LCM":
        
        def lcm(a,b):
            if a > b:
                greater = a
            else:
                greater = b

            while(True):
                if((greater % a == 0) and (greater % b == 0)):
                    lcm = greater
                    break
                greater += 1
            
            return lcm

        a = int(input("1. szám: "))
        b = int(input("2. szám: "))
        print(lcm(a,b))
            
    if n == "between(2)":

        def btw(a,b):
            while a:
                a += 1
                num.append(a)
                if a == (b - 1):
                    print(num)
                    break

        a = int(input("1. szám: "))
        b = int(input("2. szám: "))
        num = []
        print(btw(a,b))

    return c
print(calc())

temp = input("újra? (igen / nem) ")
if temp == "igen":
    print(calc())
elif temp == "nem":
    print("")
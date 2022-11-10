import turtle
def function(): 
    t = turtle.Turtle()
 
    n = int(input("Add meg a hosszúságát az alakzatnak: "))
    m = int(input("Add meg a szélességét az alakzatnak: "))

    t.forward(n)
    t.left(90)

    t.forward(m)
    t.left(90)
 
    t.forward(n)
    t.left(90)
 
    t.forward(m)
    t.left(90)

print(function())

ans = str(input("Újra? (Igen / Nem)"))

if ans == "Igen":
    print(function())
elif ans == "Nem":
    print("exiting...")
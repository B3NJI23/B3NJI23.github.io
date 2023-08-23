from random import randint

#Class:

class Car:
    def __init__(self, gyarto, modell, ferohely, toltes, tavolsag, gyartas_kezdet):
        self.gyarto = gyarto
        self.modell = modell
        self.ferohely = ferohely
        self.toltes = toltes
        self.tavolsag = tavolsag
        self.gyartas_kezdet = gyartas_kezdet

def feladat1():
    # Számláló
    counter = 0

    # 10db random szám 1 és 6 között

    nums = [str(randint(1, 6)) for x in range(10)]

    # Van-e 6-os szám a listában

    for i in nums:
        if i == "6":
            counter += 1

    # Kiíratás

    if counter > 0:
        print(
            f'1. Feladat: Darabszám meghatározása\nA generált számok: {",".join(nums)}'
        )
        print(f"A generált számok között {counter}-szor/ször/szer fordul elő a 6-os.")
    else:
        print(f"Nincs a generált számok között 6-os.")


def feladat2():
    print(f"2. Feladat: Leghosszabb szó")

    # Bekért szavak
    words = []

    # Bekérés

    for i in range(3):
        user_input = input("Kérek egy szót: ")
        words.append(user_input)

    print(f"A 3 szó közül a leghosszabb: {max(words, key=len)}")


def feladat3():
    data = []
    cars = []

    counter = 0

    with open("elekromos_autok.txt", "r", encoding="utf-8") as f:
        next(f)
        for i in f:
            counter += 1
            data.append(i.strip().split(";"))
            if len(data) == 1:
                brand, model, can_fit, charging_time, range, start_of_production = data[
                    0
                ]
                car = Car(
                    brand=brand,
                    model=model,
                    can_fit=int(can_fit),
                    charging_time=float(charging_time.replace(",", ".")),
                    range=int(range),
                    start_of_production=int(start_of_production),
                )

                cars.append(car)
                data = []

    print(f"3.2 Feladat: Elektromos autók száma: {counter} db")

    result = []

    for car in cars:
        result.append(car.range)

    print(
        f"3.3 Feladat: A megtehető távolságok átlaga: {round(sum(result) / len(result), 2)} km"
    )

    max_car = max(cars, key=lambda x: x.start_of_production)

    print(
        f"""3.4 Feladat: A legfiatalabb elektromos autó adatai
\tGyártó: {max_car.brand}
\tModell: {max_car.model}
\tSzemélyek száma: {max_car.can_fit}
\tTöltési idő: {max_car.charging_time} óra
\tMegtehető távolság: {max_car.range} km
\tGyártás kezdete: {max_car.start_of_production}"""
    )

    has_range = False

    for car in cars:
        if car.range >= 500:
            has_range = True

    if has_range == True:
        print(
            "3.5 Feladat: Van olyan autó, ami egy feltöltéssel több, mint 500km-t tud megtenni."
        )


feladat1()
feladat2()
feladat3()

users = {}

while True:
    user = input("Felhasználónév: ")
    password = input("Jelszó: ")

    if user != "stop":
        if password != "stop":
            users[user] = password
    else:
        break

print(f"\n")

with open("database.txt", "w", encoding="utf-8") as file:
    for i in users:
        print(i, users[i])
        file.writelines(f"Felhasználónév: {i}\nJelszó: {users[i]}\n\n")

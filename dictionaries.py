import json
from pathlib import Path

path = Path("slownik.json")

if path.exists():
    f = open(path, "r")
    slownik = json.load(f)
    f.close()
else:
    slownik = {}


commands = ["new_contact", "show_contacts"]
while True:
    command = input(f"Peek an option: {commands}")
    while command not in commands:
        print("Unknown command, try again")
        command = input(f"Peek an option: {commands}")
    if command == "new_contact":
        full_name = input("Podaj imie i nazwisko: ")
        b = input("Podaj numer telefonu: ")
        slownik[full_name] = b
    elif command == "show_contacts":
         print(slownik)

    answer = input("Do you want to continue Y/N? ")
    while answer.lower() not in ["y", "n"]:
        print("Choose Y or N only")
        answer = input("Do you want to continue Y/N? ")


    if answer.lower() == "n":
        f = open("slownik.json", "w")
        json.dump(slownik, f)
        f.close()
        break




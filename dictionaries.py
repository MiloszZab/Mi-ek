
slownik = {}
while True:
    command = input("Peek an option: new_contact, show_contact ")
    if command == "new_contact":
        full_name = input("Podaj imie i nazwisko: ")
        b = input("Podaj numer telefonu: ")
        slownik[full_name] = b
    elif command == "show_contact":
         print(slownik)

    command = input("Do you want to continue Y/N? ")
    if command == "N":
         break




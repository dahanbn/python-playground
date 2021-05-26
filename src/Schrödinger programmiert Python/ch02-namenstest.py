name = ""

while name != "Schrödinger":
    name = input("Wie ist dein Name: ")
    if name == "":
        print("Fehler: Kein Name eingegeben.")
    else:
        if name == "Schrödinger":
            print("Hallo Schrödinger, toller Name!")
        else:
            print("Das war wohl nichts, probiere es noch einmal.")

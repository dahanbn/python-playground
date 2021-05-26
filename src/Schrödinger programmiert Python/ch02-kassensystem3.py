
noch_einmal = "j"
while noch_einmal == "j":
    preis = input('Gib den Preis ein: ')
    rabatt_in_prozent = input("Rabatt in %: ")
    zahlung = input("Der Kunde zahlt: ")

    preis = float(preis)
    zahlung = float(zahlung)
    rabatt_in_prozent = float(rabatt_in_prozent)
    rabatt_als_betrag = preis * rabatt_in_prozent / 100
    preis_mit_rabatt = preis - rabatt_als_betrag
    rueckgeld = zahlung - preis_mit_rabatt

    print("Alter Preis: ", preis)
    print("Rabatt (" + str(rabatt_in_prozent) + "):", rabatt_als_betrag)
    print("Neuer Preis:", preis_mit_rabatt)


    print('Gegeben:', zahlung, 'rabattierter Preis:', preis_mit_rabatt)
    print('Wechselgeld:', rueckgeld)

    noch_einmal = input("Noch einmal (j): ")
    
print ("Dann nicht und tschüß!")

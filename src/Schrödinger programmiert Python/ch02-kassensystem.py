preis = input('Gib den Preis ein: ')
rabatt = input("Rabatt in %: ")
zahlung = input("Der Kunde zahlt: ")

preis = float(preis)
zahlung = float(zahlung)
rabatt = float(rabatt)
rueckgeld = zahlung - preis

print('Gegeben:', zahlung, 'Preis:', preis)
print('Wechselgeld:', rueckgeld)

erstes_wort = "Hello"
zweites_wort = "World"

print(erstes_wort)
print(zweites_wort)

first_word, second_word = "Hello", "World"

# python adds automatically a space as separator
print(first_word, second_word)

# you can change the separator string with sep
print(first_word, second_word, sep="*")

sentence = first_word + " " + second_word + "!"

print(sentence)

# you can also change the end parameter, default is end='\n'.

print(first_word, end="--")
print(second_word)

eggs = None
print(eggs)

kleine_zahl, große_zahl = 100,1
print(kleine_zahl, große_zahl)
kleine_zahl, große_zahl = große_zahl, kleine_zahl
print(kleine_zahl, große_zahl)

# pep8: naming convention - var name = lower_case_with_underscores

_wert = "Hallo"
wort1 = "Schrödinger"
wörtlich = "wie"
wort_drei = "geht's"

print(_wert, wort1, wörtlich, wort_drei, sep="-", end="?\n")

print(42 + 12.0)
print(42 + 12.0 * False)

zeichenkette = "="*10
print(zeichenkette)

eine_zahl = int("42") + 23
print(eine_zahl)

ein_text = "42" + str(23)
print(ein_text)

eggs = 20
spam = "Jeder Tag hat " + str(4 + eggs) + " Stunden"
print(spam)

eggs = int( "2" + "4")
spam = "Jeder Tag hat " + str(eggs + 12) + " Stunden"
print( spam )

eingabe = "Hello World!"
if type(eingabe) == str:
    print(eingabe, "ist ein String.")

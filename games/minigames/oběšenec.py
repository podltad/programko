import random

# Seznam slov 
slova = ['pes', 'kočka', 'pták', 'ryba', 'had', 'želva', 'krokodýl', 'lev']

def zvol_slovo():
    # Vyber náhodné slovo ze seznamu 
    return random.choice(slova)

def hra():
    slovo = zvol_slovo()
    hadane_pismena = []
    pokusy = 5

    while True:
        # Vypíše aktuální stav slova s uhádnutými písmeny
        vypis_slovo(slovo, hadane_pismena)

        if vitezstvi(slovo, hadane_pismena):
            print('Uhádl jsi! Slovo bylo:', slovo)
            break

        if pokusy == 0:
            print('Prohrál jsi! Správné slovo bylo:', slovo)
            break

        hadane_pismeno = ziskej_hadane_pismeno(hadane_pismena)

        # kontrola pokud je hádané písmeno ve slově
        if hadane_pismeno not in slovo:
            pokusy -= 1
            print('Špatné písmeno! Zbývající pokusy:', pokusy)

        # Přidá hádané písmeno do seznamu uhádnutých písmen
        hadane_pismena.append(hadane_pismeno)

def vypis_slovo(slovo, hadane_pismena):
    # Vypíše aktuální stav slova s uhádnutými písmeny
    for pismeno in slovo:
        if pismeno in hadane_pismena:
            print(pismeno, end=' ')
        else:
            print('_', end=' ')
    print()

def vitezstvi(slovo, hadane_pismena):
    # Zkontroluje, zda bylo slovo uhádnuto
    for pismeno in slovo:
        if pismeno not in hadane_pismena:
            return False
    return True

def ziskej_hadane_pismeno(hadane_pismena):
    # Získá hádané písmeno od hráče
    while True:
        hadane_pismeno = input('Zadej písmeno: ')
        hadane_pismeno = hadane_pismeno.lower()

        if len(hadane_pismeno) != 1:
            print('Zadej pouze jedno písmeno!')
        elif hadane_pismeno in hadane_pismena:
            print('Toto písmeno jsi už hádal!')
        elif not hadane_pismeno.isalpha():
            print('Zadej písmeno!')
        else:
            return hadane_pismeno

# Spuštění hry
hra()
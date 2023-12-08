class Zaměstnanec:
    def __init__(self, jméno, pozice, pobočka):
        self.jméno = jméno
        self.pozice = pozice
        self.pobočka = pobočka

class Firma:
    def __init__(self):
        self.zaměstnanci = []
        self.pobočky = set()
        self.pracovní_pozice = set()

    def přidat_zaměstnance(self, jméno, pozice, pobočka):
        zaměstnanec = Zaměstnanec(jméno, pozice, pobočka)
        self.zaměstnanci.append(zaměstnanec)
        self.pobočky.add(pobočka)
        self.pracovní_pozice.add(pozice)

    def odstranit_zaměstnance(self, jméno):
        self.zaměstnanci = [z for z in self.zaměstnanci if z.jméno != jméno]

    def zaměstnanci_v_pobočce(self, pobočka):
        return [z for z in self.zaměstnanci if z.pobočka == pobočka]

    def zaměstnanci_na_pozici(self, pozice):
        return [z for z in self.zaměstnanci if z.pozice == pozice]

    def seznam_poboček(self):
        return list(self.pobočky)

    def seznam_pracovních_pozic(self):
        return list(self.pracovní_pozice)

moje_firma = Firma()

moje_firma.přidat_zaměstnance("Petr Kozák", "Manažer", "Pobočka A")
moje_firma.přidat_zaměstnance("Eva Braunová", "Asistent", "Pobočka A")
moje_firma.přidat_zaměstnance("Lukáš Audina", "Manažer", "Pobočka B")
moje_firma.přidat_zaměstnance("Jakub Fišer", "Asistent", "Pobočka B")
moje_firma.přidat_zaměstnance("Milan Kuřina", "Uklízečka", "Pobočka C (momentálně uzavřena)")
moje_firma.přidat_zaměstnance("Jan Hronek", "Security", "Pobočka B")
moje_firma.přidat_zaměstnance("Vojtěch Hochmann", "Security", "Pobočka A")
moje_firma.přidat_zaměstnance("Jiří Minařík", "Uklízečka", "Pobočka B")
moje_firma.přidat_zaměstnance("Jakub Holík", "Manažer", "Pobočka C (momentálně uzavřena)")

print('------------------------------------------------------------')
print("Zaměstnanci v Pobočce A:")
print('------------------------------------------------------------')
for zaměstnanec in moje_firma.zaměstnanci_v_pobočce("Pobočka A"):
    print(f"{zaměstnanec.jméno} - {zaměstnanec.pozice}")
print('------------------------------------------------------------')
print("Zaměstnanci v Pobočce B:")
print('------------------------------------------------------------')
for zaměstnanec in moje_firma.zaměstnanci_v_pobočce("Pobočka B"):
    print(f"{zaměstnanec.jméno} - {zaměstnanec.pozice}")
print('------------------------------------------------------------')
print("Zaměstnanci na Pobočce C:")
print('------------------------------------------------------------')
for zaměstnanec in moje_firma.zaměstnanci_v_pobočce("Pobočka C (momentálně uzavřena)"):
    print(f"{zaměstnanec.jméno} - {zaměstnanec.pozice}")
print('------------------------------------------------------------')
print("Manažeři:")
print('------------------------------------------------------------')
for zaměstnanec in moje_firma.zaměstnanci_na_pozici("Manažer"):
    print(f"{zaměstnanec.jméno} - {zaměstnanec.pobočka}")
print('------------------------------------------------------------')
print("Seznam poboček:", moje_firma.seznam_poboček())
print("Seznam pracovních pozic:", moje_firma.seznam_pracovních_pozic())
print('------------------------------------------------------------')
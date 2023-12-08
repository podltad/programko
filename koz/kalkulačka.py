class Kalkulačka:
    def nula(self):
        return 0

    def jedna(self):
        return 1

    def dva(self):
        return 2

    def tři(self):
        return 3

    def čtyři(self):
        return 4

    def pět(self):
        return 5

    def šest(self):
        return 6

    def sedm(self):
        return 7

    def osm(self):
        return 8

    def devět(self):
        return 9

    def plus(self, x, y):
        return x + y

    def mínus(self, x, y):
        return x - y

    def krát(self, x, y):
        return x * y

    def děleno(self, x, y):
        if y != 0:
            return x / y
        else:
            return "nelze dělit nulou (to jako nevíš ?)"

Kalkulačka = Kalkulačka()

výsledek = Kalkulačka.plus(Kalkulačka.osm(), Kalkulačka.devět())
print(výsledek)  

výsledek = Kalkulačka.mínus(Kalkulačka.osm(), Kalkulačka.devět())
print(výsledek)  

výsledek = Kalkulačka.krát(Kalkulačka.čtyři(), Kalkulačka.pět())
print(výsledek)  

výsledek = Kalkulačka.děleno(Kalkulačka.osm(), Kalkulačka.dva())
print (výsledek)  

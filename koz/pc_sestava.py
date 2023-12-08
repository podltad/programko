class Produkt:
    def specifikace(self):
        pass

class počítač(Produkt):
    def __init__(self, název, CPU, ram, GPU):
        self.název = název
        self.CPU = CPU
        self.ram = ram
        self.GPU = GPU

    def specifikace(self):
        print(f'počítač - název: {self.název}, CPU: {self.CPU}, RAM: {self.ram}, GPU: {self.GPU}')

class Monitor(Produkt):
    def __init__(self, název, úhlopříčka, rozlišení, Hz):
        self.název = název
        self.úhlopříčka = úhlopříčka
        self.rozlišení = rozlišení
        self.Hz = Hz

    def specifikace(self):
        print(f'Monitor - název: {self.název}, úhlopříčka: {self.úhlopříčka}, rozlišení: {self.rozlišení}, Hz: {self.Hz}')

class klávesnice(Produkt):
    def __init__(self, název, typ, RGB):
        self.název = název
        self.typ = typ
        self.RGB = RGB

    def specifikace(self):
        print(f'klávesnice - název: {self.název}, Typ: {self.typ}, RGB: {self.RGB}')

class myš(Produkt):
    def __init__(self, název, typ, RGB):
        self.název = název
        self.typ = typ
        self.RGB = RGB

    def specifikace(self):
        print(f'myš - název: {self.název}, Typ: {self.typ}, RGB: {self.RGB}')

class Produkt_Factory:
    def vytvoř_produkt(self):
        pass

class počítač_Factory(Produkt_Factory):
    def vytvoř_produkt(self, název, CPU, ram, GPU):
        return počítač(název, CPU, ram, GPU)

class Monitor_Factory(Produkt_Factory):
    def vytvoř_produkt(self, název, úhlopříčka, rozlišení, Hz):
        return Monitor(název, úhlopříčka, rozlišení, Hz)

class klávesnice_Factory(Produkt_Factory):
    def vytvoř_produkt(self, název, typ, RGB):
        return klávesnice(název, typ, RGB)

class myš_Factory(Produkt_Factory):
    def vytvoř_produkt(self, název, typ, RGB):
        return myš(název, typ, RGB)

seznam_produktŮ = []

počítač_factory = počítač_Factory()
monitor_factory = Monitor_Factory()
klávesnice_factory = klávesnice_Factory()
myš_factory = myš_Factory()

#sestava 1

seznam_produktŮ.append(počítač_factory.vytvoř_produkt('Asus', 'AMD Ryzen 7 6800H', '16GB', 'Geforce RTX 3050 ti'))
seznam_produktŮ.append(monitor_factory.vytvoř_produkt('Samsung', '27 palců', 'full HD,', '144'))
seznam_produktŮ.append(klávesnice_factory.vytvoř_produkt('Hyper X', 'bezdrat', 'ano'))
seznam_produktŮ.append(myš_factory.vytvoř_produkt('Razer', 'drát', 'ano'))

#sestava 2

seznam_produktŮ.append(počítač_factory.vytvoř_produkt('Lenovo', 'Intel i5', '16GB', 'Geforce GTX 1650 ti'))
seznam_produktŮ.append(monitor_factory.vytvoř_produkt('Asus', '25 palců', 'full HD,', '120'))
seznam_produktŮ.append(klávesnice_factory.vytvoř_produkt('Acer', 'drát', 'ano'))
seznam_produktŮ.append(myš_factory.vytvoř_produkt('HP', 'bezdrat', 'ne'))


for produkt in seznam_produktŮ:
    produkt.specifikace()

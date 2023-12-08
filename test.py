from abc import ABC, abstractmethod
 
class Stationery(ABC):
 
    def __init__(self, name, price):
        self.name = name
        self.price = price
 
    @abstractmethod
    def getInfo(self):
        pass
 
    @abstractmethod
    def use(self):
        pass
 
class Pencil(Stationery):
 
    def getInfo(self):
        print(f"Jsem tužka {self.name} za {self.price} Kč.")
 
    def use(self):
        print("Kreslím ...")
 
class Notebook(Stationery):
 
    def getInfo(self):
        print(f"Jsem sešit {self.name} za {self.price} Kč.")
 
    def use(self):
        print("Je do mě psáno ...")
 
class Rubber(Stationery):
 
    def getInfo(self):
        print(f"Jsem guma {self.name} za {self.price} Kč.")
 
    def use(self):
        print("Gumuju ...")
 
 
class Store:
 
    article = ['Pencil', 'Notebook', 'Rubber']
    @staticmethod
    def newArticle(type, name, price):
        if type in Store.article:
            return globals()[type](name, price)
        else:
            return None
       
goods = []
goods.append(Store.newArticle('Pencil', 'AB', '7'))
goods.append(Store.newArticle('Notebook', 'A4', '35'))
goods.append(Store.newArticle('Rubber', 'pryž', '9'))
 
 
 
for i in goods:
    i.getInfo()
    i.use()
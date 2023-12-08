'''V pythonu vytvoř skript, ve kterém bude definována třída Rectangle, která bude mít dvě privátní vlatnosti 
- strany a, b, které musí být větší než 0. Součástí třídy budou gettery pro zjištění délky strany a a strany
 b. Pomocí setterů bude možné změnit hodnoty stran a, b. Metoda get_rect_content bude vracet obsah obdélníku, 
 metoda get_rect_permimeter bude vracet obvod obdélníku. Magická metoda __str__ bude vracet text v podobě
  "Obdélník o stranách a = číslo a b = číslo má obsah S = číslo a obvod O = číslo".'''

class Rectangle:
    def __init__(self, a, b):
        if a > 0 and b > 0:
            self.a = a
            self.b = b
        else:
            raise ValueError("Délka stran musí být větší než 0")

    def a(self):
        return self.a
   
    def b(self):
        return self.b
  
    def a(self, x):
        if x > 0:
            self.a = x
        else:
            raise ValueError("Délka strany musí být větší než 0")

    def b(self, y):
        if y > 0:
            self.b = y
        else:
            raise ValueError("Délka strany musí být větší než 0")

    def get_rect_content(self):
        return self.a * self.b

    def get_rect_perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return f"Obdélník o stranách: strana a = {self.a} , strana b = {self.b} , obsah S = {self.get_rect_content()} , obvod O = {self.get_rect_perimeter()}"

my_rectangle = Rectangle(6,6)
print(my_rectangle)
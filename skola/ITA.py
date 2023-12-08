# def prvocisla(n):
#     primes = []
#     for x in range(2, n + 1):
#         for y in range(2, int(x ** 0.5) + 1):
#             if x%y == 0:
#                 break
#         else:
#             primes.append(x)
#     return primes

# seznam_prvocisel = prvocisla(100)
# print(seznam_prvocisel)




# def legs(kure, krava,prase,):
#     return kure*2+prase*4 + krava*4

# print(legs(6,8,3))
    


# def skore(vyhra,remiza,prohra,):
#     return vyhra*3+remiza*1+prohra*0

# print(skore(3,4,2))


# def bool_to_str(my_bool):
#     if my_bool== True:
#         return "True"
#     elif my_bool== False:
#         return "False"
#     else:
#         return "zadej boolin"


# def devide(a,b):
#     if a/b >= a//b + 0.5:
#         return a//b + 1
#     else:
#         return a//b

# print(devide(7,3))
     

# def zbytek_po_deleni(a,b):
#     if a%b == 0
#     return True
# else:
#     return False



# An= An-2 + An-1

# x = abs(int(input("Type any positive number:")))
# n1, n2= 0,1
# count = 0
# while count < x :
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1

# _______________________________________________

# def fibonaci(a,b,c):
#     x=0
#     fib = [0]
#     while x<=c:
#          fib.append(b)
#          a,b = b , a+b
#          x+=1 
#     return fib
# print(fibonaci(0,1,10))
    


# def discount(price, percent):
#   """
#     Funkce má dvě vstupní hodnoty - cena produktu a slevu v procentech. Vypočítejte,
#     jaká bude cena produktu po slevě.
    
#     >>> discount(1500, 50)
#     750.0
#     """
    
#     procent = price /100
#     var = percent * procent

#     return(price-var)

#     print(discount(1500,50))






# def dps(damage, attacks, time, timespan):
#     """
#     Napište funkci na výpočet dps (damage per second). Na vstupu budou tři hodnoty -
#     výše dmg za jeden útok, počet útoků za sekundu, časová jednotka a délka času.

#     >>> dps(40, 5, 'second', 3)
#     600
#     >>> dps(100, 1, 'minute', 15)
#     90000
#     >>> dps(2, 100, 'hour', 1)
#     720000
#     """
    
#     return ()


# def color_invert(Red, Green, Blue):
#     """
#     Napište funkci color_invert, které bude invertovat barvy zapsané
#     ve formátu RGB. Tyto barvy se zapisují stylem (255, 255, 255), 
#     kde první hodnota značí hodnotu červené barvy, druhá hodnota značí
#     hodnotu zelené barvy a třetí hodnota značí hodnotu modré barvy.
#     každá barva má hodnotu od 0 do 255.

#     >>> color_invert(255,255,255)
#     (0, 0, 0)
#     >>> color_invert(165,170,221)
#     (90, 85, 34)
#     """

#     return ()

# def distance(xa, ya, xb, yb):
#     """
#     Funkce vypočítá vzdálenost dvou bodů A a B v rovině.
#     Body jsou zadané dvojicí souřadnic A(xa, ya), B(xb, yb)

#     >>> distance(0, 0, 3, 4)
#     5.0
#     """

#     return ()

# def list_swap(list, old_num, new_num):
#     """
#     Funkce vymění hodnoty old_num za hodnotu new_num v zadaném listu.

#     >>> list_swap([1,5,3,6,5], 5, 0)
#     [1, 0, 3, 6, 0]
#     """

#     return ()

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
   
    
    
    
    
#   Vytvořte funkci, která převede první písmeno na konec slova a přidá 'ay'.  
    
# def pig_latin(word):

#   return(word[1 :]+word[0]*"ay")
  





# def card_hide(card_num):
#     """
#     Vytvořte funkci, která skyje prvních dvanáct čísel kreditní karty.

#     >>> card_hide("1234123456785678")
#     '************5678'

#     >>> card_hide("8754456321113213")
#     '************3213'
#     """





#   return"*"*12 + card_num[12:] 

#   print(card_hide("1234123456785678"))





  


# def pig_latin(word):
#   return(word[1 :]+word[0]+"ay")
# print (pig_latin("adam"))
  


  





# def pig_latin(world):
#   return(world[1 :]+world[0+"ay"])

# a = input("zadejte větu:")
# b = a.split()

# for world in b:
#   world=(world[1 :]+world[0]+"ay")
#   print(world)


















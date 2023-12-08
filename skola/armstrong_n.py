num = int(input("vložte číslo: "))
x = 0
y = num
while y > 0:
   digit = y % 10
   x += digit ** 3
   y //= 10
if num == x:
   print(num,"je to armstong číslo")
else:
   print(num,"není to armstong číslo")
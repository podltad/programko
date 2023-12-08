from collections import Counter
list = ['Novak','Hroch','Novak','Kos','Vrabec','Hroch','Hroch',]
counter = Counter(list)
nejčastějsíSL = counter.most_common(1)[0]
print(f"Nejčastěji Příjmení: {nejčastějsíSL[0]}, Počet: {nejčastějsíSL[1]}")
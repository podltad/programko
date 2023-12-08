

def lamps_on_street(x): 
    x += " "
    y = ""
    for i in range(len(x)):
        if i == 0:
            y += x[i]

        elif x[i] == "X":
            y += x[i]
        elif x[i+1]==" ":
            y += x[i]
            return y
        elif y[len(y)-1]== "-":
            y += "O"
            continue
        elif x[i-1] == "O" and x[i+1] =="O":
            y += "-"
        else :
            y += x[i]
    return y


print(lamps_on_street("OOOXOXOOOOOO"))

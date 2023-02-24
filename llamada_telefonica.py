#input
num_min = int(input("digite el valor de num_min: "))

#processing

if num_min < 4:
    y = 300
else:
    y = (num_min * 50) + 300 - 150

if y > 999:
    msj = " mil"
else:
    msj = " pesos"

#output

print("el costo de la llamada es de " + str(y) + msj)
print("Calculadora de determinantes para vectores.")

print("Ingrese el primer vector")
first_x = int(input("Respecto al eje X: "))
first_y = int(input("Respecto al eje Y: "))
first_z = int(input("Respecto al eje Z: "))

print("De acuerdo, ahora ingrese el segundo vector")
second_x = int(input("Respecto al eje X: "))
second_y = int(input("Respecto al eje Y: "))
second_z = int(input("Respecto al eje Z: "))

cross_x = first_y * second_z - first_z * second_y
cross_y = first_z * second_x - first_x * second_z
cross_z = first_x * second_y - first_y * second_x

if cross_x == 0 and cross_y == 0 and cross_z == 0:
    print("Los vectores son paralelos.")
else:
    if cross_x == 0:
        cross_x = ''
    elif cross_x == 1:
        cross_x = 'i'
    elif cross_x == -1:
        cross_x = '-i'
    else:
        if cross_x < 0:
            cross_x = str(cross_x) + 'i'
        elif cross_x > 0:
            cross_x = '+' + str(cross_x) + 'i'

    if cross_y == 0:
        cross_y = ''
    elif cross_y == 1:
        cross_y = 'j'
    elif cross_y == -1:
        cross_y = '-j'
    else:
        if cross_y < 0:
            cross_y = str(cross_y) + 'j'
        elif cross_y > 0:
            cross_y = '+' + str(cross_y) + 'j'   

    if cross_z == 0:
        cross_z = ''
    elif cross_z == 1:
        cross_z = 'k'
    elif cross_z == -1:
        cross_z = '-k'
    else:
        if cross_z < 0:
            cross_z = str(cross_z) + 'k'
        elif cross_z > 0:
            cross_z = '+' + str(cross_z) + 'k'
    print(f"El vector resultante es: {cross_x}{cross_y}{cross_z}")
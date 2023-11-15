#Version larga
def findNeedle(areglo: list)-> str:
    for indice,texto in enumerate(areglo):
        if texto == "needle":
            posicionIndex = indice
            break
    return f"la aguja se encuentra en la posicion numero {posicionIndex}"


#Version corta
# def findNeedle(arreglo: list)-> str:
#     return  f"la aguja se encuentra en la posicion numero " + str(arreglo.index("needle"))

array = ["hay", "junk", "hay", "moreJunk", "needle", "randomJunk"]

print(findNeedle(array))
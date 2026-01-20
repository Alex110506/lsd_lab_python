from functools import reduce

def parc(key,lista):
    if(len(lista) == 0):
        return 0

    print(key,'-',lista[0])

    return parc(key,lista[1:])

def parc1(key,lista):
    if(len(lista) == 0):
        return 0

    if(key<=lista[0]):
        print(key,'-',lista[0])

    return parc1(key,lista[1:])

def arce(graf):
    gr=reduce(lambda acc,x: parc(x,graf[x]), graf.keys(), 0)
    return

def muchii(graf):
    gr=reduce(lambda acc,x: parc1(x,graf[x]), graf.keys(), 0)

graf={1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}
arce(graf)
print("")
muchii(graf)
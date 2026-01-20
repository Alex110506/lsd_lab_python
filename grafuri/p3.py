def add(graf,nod,lista):
    graf[nod]=lista
    return

def adaugare(graf,lista,nod):
    if(len(lista)==0):
        return graf

    if(nod not in graf[lista[0]]):
        graf[lista[0]].append(nod)

    return adaugare(graf,lista[1:],nod)

def addor(graf,nod,lista):
    graf[nod]=lista
    adaugare(graf,lista,nod)
    return

graf={1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}
add(graf,5,[1,2,3])

addor(graf,6,[1,2,3])
print(graf)
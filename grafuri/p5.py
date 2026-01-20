from functools import reduce

def f(acc,lista,nod):
    if(len(lista)==0):
        return acc

    if(nod**2 in acc):
        acc[nod**2].append(lista[0]**2)
    else:
        acc[nod**2] = [lista[0]**2]

    return f(acc,lista[1:],nod)

def schimb(graf):
    newg=reduce(lambda acc,x: f(acc,graf[x],x),graf.keys(),dict())
    graf=newg
    return graf

graf={1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}
print(schimb(graf))
from functools import reduce

def parc(acc,lista,stegere,key):
    if(len(lista)==0):
        return acc

    if((key,lista[0]) not in stegere):
        if(key in acc):
            acc[key].append(lista[0])
        else:
            acc[key]=[lista[0]]

    return parc(acc,lista[1:],stegere,key)


def sterge(graf,lista):
    newg=reduce(lambda acc,x: parc(acc,graf[x],lista,x),graf.keys(),dict())
    return newg

graf={1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}
lista=[(2,1), (3,1)]

graf=sterge(graf,lista)
print(graf)
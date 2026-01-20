def fori(graf,n1,n2):
    if(n2 in graf[n1]):
        return False
    else:
        graf[n1].append(n2)
        return True

def fnor(graf,n1,n2):
    if(n2 in graf[n1]):
        return False
    else:
        graf[n1].append(n2)
        graf[n2].append(n1)
        return True


graf={1:[2,3,4], 2:[1,3], 3:[1,4], 4:[1,3]}
print(fori(graf,2,4))
print(graf)
print(fnor(graf,3,2))
print(graf)

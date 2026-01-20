def gaseste_maxim(node):
    current = node
    while current["right"] is not None:
        current = current["right"]
    return current["value"]

def elim(arb,val):
    if(arb==None):
        return None

    if(val==arb["value"]):
        if(arb["left"]==None and arb["right"]==None):
            return None
        if(arb["left"]==None and arb["right"]!=None):
            return arb["right"]
        if(arb["right"]==None and arb["left"]!=None):
            return arb["left"]
        if(arb["left"]!=None and arb["right"]!=None):
            val_max=gaseste_maxim(arb["left"])
            arb["value"]=val_max
            arb["left"]=elim(arb["left"],val_max)
            return arb
    else:
        if(val<arb["value"]):
            arb["left"]=elim(arb["left"],val)
        else:
            arb["right"]=elim(arb["right"],val)

    return arb


arb= { "value" : 2, "left":
        {
            "value": 7, "left": None, "right":
            {
                "value": 6, "left":
                {
                    "value": 5, "left": None, "right": None
                }, "right":
                {
                    "value":11, "left": None, "right": None
                },
            },
        }, "right":
            {
                "value": 4, "left": None, "right": None
            }
    }

arb= elim(arb,6)
print(arb)


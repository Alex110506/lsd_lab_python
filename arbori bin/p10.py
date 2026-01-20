def niv(arb,nod,nivel=0):
    if(arb==None):
        return 0

    if(arb["value"]==nod):
        return nivel

    return niv(arb["left"],nod,nivel+1)+niv(arb["right"],nod,nivel+1)

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

print(niv(arb,2))
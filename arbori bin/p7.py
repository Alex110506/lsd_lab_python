def cond(arb,f):
    if(arb==None):
        return []
    if(f(arb["value"])==True):
        return [arb["value"]]+cond(arb["left"],f) + cond(arb["right"],f)

    return cond(arb["left"],f) + cond(arb["right"],f)

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

print(cond(arb,lambda x:x>3))
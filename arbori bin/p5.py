def nivell(arb,nivel=0):
    if(arb==None):
        return nivel

    return max(nivell(arb["left"],nivel+1),nivell(arb["right"],nivel+1),nivel)

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

print(nivell(arb))
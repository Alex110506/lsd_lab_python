def nonf(arb):
    if(arb==None):
        return 0

    if(arb["left"]!=None or arb["right"]!=None):
        return 1 + nonf(arb["left"]) + nonf(arb["right"])
    else:
        return nonf(arb["left"])+nonf(arb["right"])


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

print(nonf(arb))
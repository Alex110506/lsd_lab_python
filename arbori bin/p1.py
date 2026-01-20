def parc(arb):
    if(arb == None):
        return 0

    if((arb["left"]==None and arb["right"] != None) or(arb["left"]!=None and arb["right"]==None)):
        print(arb["value"])

    return parc(arb["left"])+parc(arb["right"])



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

parc(arb)
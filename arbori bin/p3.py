def parc(arb,depth=0):
    if(arb==None):
        return 0

    if(depth==0):
        print(arb["value"])
    else:
        print(" "*(2*depth-1),arb["value"])

    return parc(arb["left"],depth+1)+parc(arb["right"],depth+1)

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
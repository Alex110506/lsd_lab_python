def niv(arb,nivel,nivcurr=0):
    if(arb==None):
        return 0

    if(nivel==nivcurr):
        print(arb["value"])

    return niv(arb["left"],nivel,nivcurr+1)+niv(arb["right"],nivel,nivcurr+1)

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

niv(arb,3)
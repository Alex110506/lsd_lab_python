def minmax(arb):
    if(arb["left"]==None and arb["right"]==None):
        return (arb["value"],arb["value"])
    if(arb["left"]!=None and arb["right"]==None):
        return (min(minmax(arb["left"])[0],arb["value"]),max(minmax(arb["left"])[1],arb["value"]))
    if(arb["right"]!=None and arb["left"]==None):
        return (min(minmax(arb["right"])[0],arb["value"]),max(minmax(arb["right"])[1],arb["value"]))

    return (min(minmax(arb["left"])[0],minmax(arb["right"])[0],arb["value"]),max(minmax(arb["left"])[1],minmax(arb["right"])[1],arb["value"]))


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

print(minmax(arb))
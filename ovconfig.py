worlds["alfa"] = "/minecraft/alfa/world"
worlds["bravo"] = "/minecraft/bravo/world"
worlds["charlie"] = "/minecraft/charlie/world"
worlds["delta"] = "/minecraft/delta/world"

rendermode = "smooth_lighting"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]

renders["alfaN"] = {
    "world": "alfa",
    "title": "Nord",
    "northdirection" : "upper-left",
}

renders["alfaW"] = {
    "world": "alfa",
    "title": "Ouest",
    "northdirection" : "lower-left",
}

renders["alfaS"] = {
    "world": "alfa",
    "title": "Sud",
    "northdirection" : "lower-right",
}

renders["alfaE"] = {
    "world": "alfa",
    "title": "Est",
    "northdirection" : "upper-right",
}

renders["alfaCave"] = {
    "world": "alfa",
    "title": "Cave",
    "rendermode": my_cave
}

renders["bravoN"] = {
    "world": "bravo",
    "title": "Nord",
    "northdirection" : "upper-left",
}

renders["bravoW"] = {
    "world": "bravo",
    "title": "Ouest",
    "northdirection" : "lower-left",
}

renders["bravoS"] = {
    "world": "bravo",
    "title": "Sud",
    "northdirection" : "lower-right",
}

renders["bravoE"] = {
    "world": "bravo",
    "title": "Est",
    "northdirection" : "upper-right",
}

renders["bravoCave"] = {
    "world": "bravo",
    "title": "Cave",
    "rendermode": my_cave
}

renders["charlieN"] = {
    "world": "charlie",
    "title": "Nord",
    "northdirection" : "upper-left",
}

renders["charlieW"] = {
    "world": "charlie",
    "title": "Ouest",
    "northdirection" : "lower-left",
}

renders["charlieS"] = {
    "world": "charlie",
    "title": "Sud",
    "northdirection" : "lower-right",
}

renders["charlieE"] = {
    "world": "charlie",
    "title": "Est",
    "northdirection" : "upper-right",
}

renders["charlieCave"] = {
    "world": "charlie",
    "title": "Cave",
    "rendermode": my_cave
}

renders["deltaN"] = {
    "world": "delta",
    "title": "Nord",
    "northdirection" : "upper-left",
}

renders["deltaW"] = {
    "world": "delta",
    "title": "Ouest",
    "northdirection" : "lower-left",
}

renders["deltaS"] = {
    "world": "delta",
    "title": "Sud",
    "northdirection" : "lower-right",
}

renders["deltaE"] = {
    "world": "delta",
    "title": "Est",
    "northdirection" : "upper-right",
}

renders["deltaCave"] = {
    "world": "delta",
    "title": "Cave",
    "rendermode": my_cave
}



outputdir = "/minecraft/mcmap"


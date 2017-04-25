worlds["alfa"] = "/minecraft/alfa/world"
worlds["bravo"] = "/minecraft/bravo/world"
worlds["charlie"] = "/minecraft/charlie/world"
worlds["delta"] = "/minecraft/delta/world"

rendermode = "smooth_lighting"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]

renders["alfaN"] = {
    "world": "alfa",
    "title": "alfa N",
    "northdirection" : "upper-left",
}

renders["alfaW"] = {
    "world": "alfa",
    "title": "alfa W",
    "northdirection" : "lower-left",
}

renders["alfaS"] = {
    "world": "alfa",
    "title": "alfa S",
    "northdirection" : "lower-right",
}

renders["alfaE"] = {
    "world": "alfa",
    "title": "alfa E",
    "northdirection" : "upper-right",
}

renders["bravoN"] = {
    "world": "bravo",
    "title": "bravo N",
    "northdirection" : "upper-left",
}

renders["bravoW"] = {
    "world": "bravo",
    "title": "bravo W",
    "northdirection" : "lower-left",
}

renders["bravoS"] = {
    "world": "bravo",
    "title": "bravo S",
    "northdirection" : "lower-right",
}

renders["bravoE"] = {
    "world": "bravo",
    "title": "bravo E",
    "northdirection" : "upper-right",
}

renders["charlieN"] = {
    "world": "charlie",
    "title": "charlie N",
    "northdirection" : "upper-left",
}

renders["charlieW"] = {
    "world": "charlie",
    "title": "charlie W",
    "northdirection" : "lower-left",
}

renders["charlieS"] = {
    "world": "charlie",
    "title": "charlie S",
    "northdirection" : "lower-right",
}

renders["charlieE"] = {
    "world": "charlie",
    "title": "charlie E",
    "northdirection" : "upper-right",
}

renders["deltaN"] = {
    "world": "delta",
    "title": "delta N",
    "northdirection" : "upper-left",
}

renders["deltaW"] = {
    "world": "delta",
    "title": "delta W",
    "northdirection" : "lower-left",
}

renders["deltaS"] = {
    "world": "delta",
    "title": "delta S",
    "northdirection" : "lower-right",
}

renders["deltaE"] = {
    "world": "delta",
    "title": "delta E",
    "northdirection" : "upper-right",
}

renders["deltaCave"] = {
    "world": "delta",
    "title": "delta cave",
    "rendermode": my_cave
}



outputdir = "/minecraft/mcmap"


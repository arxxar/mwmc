def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
    
def signFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
    
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
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["alfaCave"] = {
    "world": "alfa",
    "title": "Cave",
    "rendermode": my_cave,
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["bravoN"] = {
    "world": "bravo",
    "title": "Nord",
    "northdirection" : "upper-left",
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["bravoCave"] = {
    "world": "bravo",
    "title": "Cave",
    "rendermode": my_cave,
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["charlieN"] = {
    "world": "charlie",
    "title": "Nord",
    "northdirection" : "upper-left",
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["charlie"] = {
    "world": "charlie",
    "title": "Cave",
    "rendermode": my_cave,
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["deltaN"] = {
    "world": "delta",
    "title": "Nord",
    "northdirection" : "upper-left",
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

renders["deltaCave"] = {
    "world": "delta",
    "title": "Cave",
    "rendermode": my_cave,
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

outputdir = "/minecraft/mcmap"

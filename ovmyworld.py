def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

worlds["MyWorld"] = "/minecraft/" + os.environ['MYWORLD'] + "/world"

rendermode = "smooth_lighting"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]


renders["deltaN"] = {
    "world": "MyWorld",
    "title": "Nord",
    "northdirection" : "upper-left",
}


renders["deltaCave"] = {
    "world": "MyWorld",
    "title": "Cave",
    "rendermode": my_cave
}

outputdir = "/minecraft/mcmap"

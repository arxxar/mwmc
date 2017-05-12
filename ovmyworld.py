import os

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

MYWORLD = os.environ["MYWORLD"]
    
worlds[MYWORLD] = "/minecraft/" + MYWORLD + "/world"

rendermode = "smooth_lighting"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]


renders["MyWorldN"] = {
    "world": MYWORLD,
    "title": "Nord",
    "northdirection" : "upper-left",
}


renders["MyWorldCave"] = {
    "world": MYWORLD,
    "title": "Cave",
    "rendermode": my_cave
    'markers': [dict(name="Players", filterFunction=playerIcons)]
}

outputdir = "/minecraft/mcmap/"

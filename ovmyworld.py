import os

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
    
def chestFilter(poi):
    if poi['id'] == "Chest":
        return ("Chest", "Chest with %d items" % len(poi['Items']))

MYWORLD = os.environ["MYWORLD"]
    
worlds[MYWORLD] = "/minecraft/" + MYWORLD + "/world"

rendermode = "smooth_lighting"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]


renders["MyWorldN"] = {
    "world": MYWORLD,
    "title": "Nord",
    "northdirection" : "upper-left",
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Chests", filterFunction=chestFilter)],
}


renders["MyWorldCave"] = {
    "world": MYWORLD,
    "title": "Cave",
    "rendermode": my_cave,
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Chests", filterFunction=chestFilter)],
}

outputdir = "/minecraft/mcmap/"

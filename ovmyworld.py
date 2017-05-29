import os

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
    
def signFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

MYWORLD = os.environ["MYWORLD"]
    
worlds[MYWORLD] = "/minecraft/" + MYWORLD + "/world"

rendermode = "smooth_lighting"
my_cave = [Base(), EdgeLines(), Cave(only_lit=True), DepthTinting()]


renders["MyWorldN"] = {
    "world": MYWORLD,
    "title": "Nord",
    "northdirection" : "upper-left",
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}


renders["MyWorldCave"] = {
    "world": MYWORLD,
    "title": "Cave",
    "rendermode": my_cave,
    "markers": [dict(name="Players", filterFunction=playerIcons),
                dict(name="Signs", filterFunction=signFilter)],
}

outputdir = "/minecraft/mcmap/"

import os

layersDict = {
    "Anvil": "Anvil",
    "AlBasrah": "Al Basrah",
    "Belaya": "Belaya Pass",
    "Chora": "Chora",
    "Fallujah": "Fallujah",
    "FoolsRoad": "Fool's Road",
    "GooseBay": "Goose Bay",
    "Gorodok": "Gorodok",
    "JensensRange": "Jensen's Range",
    "Kamdesh": "Kamdesh Highlands",
    "Kohat": "Kohat Toi",
    "Kokan": "Kokan",
    "LashkarValley": "Lashkar Valley",
    "Logar": "Logar Valley",
    "Manic": "Manic-5",
    "Mestia": "Mestia",
    "Mutaha": "Mutaha",
    "Narva": "Narva",
    "Skorpo": "Skorpo",
    "Sumari": "Sumari Bala",
    "Tallil": "Tallil Outskirts",
    "Yehorivka": "Yehorivka"
}

with open('layers.txt') as layersFile:
    lines = layersFile.readlines()
    lines = [line.rstrip() for line in lines]

# for line in lines:
    #
with open('output.html', 'w') as outputFile:
    outputFile.write("""<section class="headers_section">\n""")
    for key in layersDict.keys():
        outputFile.write("""\t<a class="headers" href="#""" +
                         key + """">""" + layersDict[key] + """</a>\n""")
    outputFile.write("""</section>\n""")
    for key in layersDict.keys():
        outputFile.write("""<section id=""" + key + """>\n""")
        outputFile.write("""\t<h2>""" + layersDict[key] + """</h2>\n""")
        for line in lines:
            if key in line:
                MapName = line.replace("_", " ")
                LayerName = MapName.replace(
                    key, '').replace('  ', ' ').strip()
                useLazy = ' loading="lazy"' if key != "Anvil" else ""
                # Watch out for CAF layers cause the names are inconsistent there...
                element = "\t<div><a href=\"img/maps/full_size/{line}.jpg\"><picture><source srcset=\"img/maps/webp/{line}.webp\" type=\"image/webp\"><source srcset=\"img/maps/thumbnails/{line}.jpg\" type=\"image/jpeg\"><img src=\"img/maps/thumbnails/{line}.jpg\" alt=\"{mapName}\"{lazy}></picture></a><h3>{layerName}</h3><a class=\"vehicles\" onclick=\"view_vehicles('{line}')\"><picture><source srcset=\"img/icons/vehicles.webp\" type=\"image/webp\"><source srcset=\"img/icons/vehicles.png\" type=\"image/png\"><img src=\"img/icons/vehicles.png\" alt=\"Vehicles\"{lazy}></picture></a></div>\n".format(
                    mapName=MapName, layerName=LayerName, line=line, lazy=useLazy)
                outputFile.write(element)
        outputFile.write("""</section>\n""")

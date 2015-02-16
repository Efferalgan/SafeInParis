import xmltodict
import json
from unidecode import unidecode

input_file = open("commissariats.kml")
output_file = open("commissariats.json","w+")
obj = xmltodict.parse(input_file.read())

#print(obj['osm']['node'][0]['@id'])
for i in range(len(obj['kml']['Document']['Placemark'])):

    myNode = obj["kml"]["Document"]["Placemark"][i]
    styleUrl = myNode["styleUrl"]
    if(styleUrl == "#paris"):
       lonlat = myNode["Point"]["coordinates"].split(",")
       myDeepNode = myNode["ExtendedData"]["SchemaData"]["SimpleData"]
       myInfo = ""
       for j in range(len(myDeepNode)):
           if(myDeepNode[j]["@name"] == "Commissariat"):
			   myInfo = unidecode(myDeepNode[j]["#text"])
       output_file.write("{\"geom_x_y\":["+lonlat[0]+","+lonlat[1]+"],\"info\":\""+myInfo+"\"}\n")

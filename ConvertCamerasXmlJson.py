import xmltodict
import json

input_file = open("cameras.xml")
output_file = open("cameras.json","w+")
obj = xmltodict.parse(input_file.read())


#print(obj['osm']['node'][0]['@id'])
for i in range(len(obj['osm']['node'])):

    myNode = obj["osm"]["node"][i];
    lon = float(myNode["@lon"])
    lat = float(myNode["@lat"])
    if (lon < 2.47 and lon > 2.25 and lat < 48.91 and lat > 48.81): #a square centered on Paris
        myTag = myNode["tag"]
        myInfo = "unknown"
        
        if (type(myTag) is list):
            lengthOfTag = len(myTag)
            for j in range(lengthOfTag):
                if (myTag[j]["@k"] == "camera:type"):
                    myInfo = myTag[j]["@v"]
                    break  
        else:
            if (myTag["@k"] == "camera:type"):
                myInfo = mytag["@v"]
                
        output_file.write("{\"geom_x_y\":["+str(lon)+","+str(lat)+"],\"info\":\""+myInfo+"\"}\n")

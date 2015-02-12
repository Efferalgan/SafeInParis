import csv
import json
import unicodedata

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD',unicode(input_str, 'utf8'))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

csvfile = open('eclairage_paris.csv', 'r')
jsonfile = open('eclairage.json', 'w')

fieldnames = csvfile.readline().replace("\n", "").replace("\r","").split(",")

reader = csv.DictReader(csvfile, fieldnames)
listOfItems = ["info","geom"]

for row in reader:
	if(row):
		for item in listOfItems:
			row[item] = remove_accents(row[item])
		coord = row["geom_x_y"].replace(" ","").replace("[","").replace("]","").split(",")
		jsonfile.write("{\"geom_x_y\":["+coord[1]+","+coord[0]+"],\"info\":\""+row["info"].replace("provisoie","provisoire")+"\"}\n")

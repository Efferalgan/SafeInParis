import sys

collection = sys.argv[1]

jsonfile = open(collection+'db.json', 'r')
jsfile = open(collection+'.jsonp', 'w')

jsfile.write(collection +" = [");

for row in jsonfile:
	jsfile.write(row.replace("\n",",\n"))
		
jsfile.write("]")

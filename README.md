# SafeInParis

##The goal:
Visualising data about safety in Paris on a map, in order to be able to avoid no-go-zones at night. (Or to commit crimes unnoticed.)

##The data:
For now, the map allows to visualise:
- street lights, a white circle of radius 20m is drawn around regular ones, a 60m around huge lightings, and a 8m around small light;
- cameras, also 20m, blue color;
- police stations, a green circle of radius 330m is drawn around them. It roughly corresponds to the distance one can sprint in one minute (assuming running speed of 20km/h).

##How it works:
Clone the directory, install the needed libraries (see below), run Global_Import.py, run Global_Export.py, and you're done.

###The Python libraries you need to have:
- unidecode (pip install unidecode OR apt-get install python-unidecode)
- xmltodict (pip install xmltodict OR apt-get install xmltodict)

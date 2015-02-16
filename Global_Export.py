import subprocess

subprocess.call(["mongoexport","-d","global","-c","eclairage","-o","eclairagedb.json"])
print("Export de l'eclairage depuis mongodb reussi")
subprocess.call(["mongoexport","-d","global","-c","cameras","-o","camerasdb.json"])
print("Export des cameras depuis mongodb reussi")
subprocess.call(["mongoexport","-d","global","-c","commissariats","-o","commissariatsdb.json"])
print("Export des commissariats depuis mongodb reussi")
subprocess.call(["python","ConvertJsonJs.py","eclairage"])
subprocess.call(["python","ConvertJsonJs.py","cameras"])
subprocess.call(["python","ConvertJsonJs.py","commissariats"])
print("Conversions reussies")
subprocess.call(["chromium","Test_OpenLayer4.html"])

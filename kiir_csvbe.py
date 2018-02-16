import json
import csv

db = 49220

def szures(s):
	s = s.lower()
	s = s.replace("\u00e0", "a")
	s = s.replace("\u0103", "a")
	s = s.replace("\u00e1", "a")
	s = s.replace("\u00e2", "a")
	s = s.replace("\u0391", "a")
	s = s.replace("\u03b1", "a")
	
	s = s.replace("\u00e9", "e")
	s = s.replace("\u00e8", "e")
	
	s = s.replace("\u00ed", "i")
	s = s.replace("\u00ec", "i")
	s = s.replace("\u00ee", "i")
	
	s = s.replace("\u00f3", "o")
	s = s.replace("\u00f6", "o")
	s = s.replace("\u0151", "o")
	s = s.replace("\u039f", "o")
	
	s = s.replace("\u039b", "l")
	
	s = s.replace("\u00fa", "u")
	s = s.replace("\u0171", "u")
	s = s.replace("\u00fc", "u")
	s = s.replace("\u016b", "u")
	
	s = s.replace("\u015f", "s")
	s = s.replace("\u0219", "s")
	
	s = s.replace("\u021b", "t")
	s = s.replace("\u0163", "t")
	
	s = s.replace("\u0e4f", "")
	s = s.replace("\u032f", "")
	s = s.replace("\u0361", "")
	
	return s

with open("proba.txt") as f:
	s = f.read()
s = szures(s)
data = json.loads(s)

with open("data.csv", "w", newline="") as file:
	h = ["id", "name", "birth", "livesin", "studwhere", "studyear", "workwhere", "workwhat"]
	writer = csv.DictWriter(file, fieldnames = h)
	writer.writeheader()
	db = 0
	for i in data:
		#print(type(i))
		try:
			writer.writerow({h[0]: i["id"], h[1]:szures(i["name"]), h[2]:szures(i["birth"]), h[3]:szures(i.get("livesin", "")), h[4]:szures(i.get("studwhere", "")), h[5]:i.get("studyear", ""), h[6]:szures(i.get("workwhere", "")), h[7]:szures(i.get("workwhat", ""))})
		except:
			db = db + 1
	print(db)
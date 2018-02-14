import json

db = 49220

#with open("proba.txt") as f:
#	data = json.loads(f.read())

#print(data)
#print(type(data[1]))
#print("----")

with open("dataset.txt") as file:
	line = file.read()

line = line[1:-1] #kiszurjuk a [] -t

darabok = line.split('{') #szetvagjuk a {} -k menten
data_strings = []
for i in darabok:
	data_strings.append(i[:-3]) # levagja a }, -t

data = []
for i in data_strings:
	data.append(json.loads('{' + i + '}'))

print(data[2]["livesin"])
print(type(data[2]))
print(data[2:5])
# -*- coding: utf-8 -*-
import geocoder
import csv

# Recibe la ruta de un csv y devuelve un array de puntos
# El array de puntos contiene todas las columnas del csv
def getPoints(csvFile, fieldNameAddress, delimiter=',', quoting='"', decodeTo='utf8'):
	g = []
	i = 0 
	with open(csvFile) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			direc = row[fieldNameAddress]
			direc = direc.decode(decodeTo)
			tmp_g = geocoder.osm(direc)
			listRow = []
			for key in row:
				listRow.append(row[key])

			try:
				listRow.append(tmp_g.x)
				listRow.append(tmp_g.y)
			except:
				listRow.append("err")
				listRow.append("err")
			
			#print(tmp_g.x)
			#print(tmp_g.y)
			g.append(listRow)
			i = i + 1
			print(i)
			print(listRow)
					
	return g
	
def writeCsv(mzPoints, fileTarget):
	with open(fileTarget, 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
		spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


puntos = getPoints('/tmp/personas2000.csv', 'Direccion')
with open("/tmp/puntos.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(puntos)

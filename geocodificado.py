# -*- coding: utf-8 -*-
import geocoder
import csv

# Recibe la ruta de un csv y devuelve un array de puntos
# El array de puntos contiene todas las columnas del csv
def getPoints(csvFile, fieldNameAddress, delimiter=',', quoting='"', decodeTo='utf8'):
	g = []
	with open(csvFile) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			direc = row[fieldNameAddress]
			direc = direc.decode(decodeTo)
			tmp_g = geocoder.google(direc)
			listRow = []
			for key in row:
				listRow.append(row[key])

			try:
				listRow.append(tmp_g.latlng[0])
				listRow.append(tmp_g.latlng[1])
			except:
				listRow.append("err")
				listRow.append("err")

			g.append(listRow)		
	return g
	
def writeCsv(mzPoints, fileTarget):
	with open(fileTarget, 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
		spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


puntos = getPoints('/tmp/personas.csv', 'Direccion')
with open("/tmp/puntos.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(puntos)

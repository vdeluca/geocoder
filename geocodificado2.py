# -*- coding: utf-8 -*-
import geocoder
import csv

g = []
n = 0
direc = ""
with open('/tmp/39personas.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		#print(row['Direccion'])
		direc = row['Direccion']
		direc = direc.decode('utf8')
		tmp_g = geocoder.google(direc)
		n = n + 1
		print(tmp_g.latlng[0])

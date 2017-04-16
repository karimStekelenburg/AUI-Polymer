#!/usr/bin/env python
from helpers import *

def newFiets(fiets):
		if fiets['regDate'] == "":
				return "date empty"
		try:
				validateDate(fiets['regDate'])
		except ValueError:
				return "date format incorrect, please use YYYY-MM-DD format"

		if fiets['status'] == "":
				fiets['status'] = "verhuurbaar"

		if fiets['status'] != "verhuurt" and fiets['status'] != "verhuurbaar" and fiets['status'] != "in onderhoud":
				return "status unknown"


		try:
				query = ("INSERT INTO `Fietsen`(regDate, status, notes) VALUES (%s,%s,%s)")
				values = (fiets['regDate'],fiets['status'], fiets['notes'])
				db.cursor.execute(query,values)
				db.cnx.commit()
				return "success"
		except:
				return "sql error"


db = sqlHandler.DbInterface(dbConfig.db)
fiets = jsonHandler.deserializeJson()
response = {"errorCode": newFiets(fiets)}
jsonHandler.serializeJson(response)
db.close()
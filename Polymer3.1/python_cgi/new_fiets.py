#!/usr/bin/env python
from helpers import *

def newFiets(fiets):
		db.cursor.execute("INSERT INTO `Fietsen`(regDate, status, notes) VALUES (%s,%s,%s)" % (fiets['regDate'],fiets['status'], fiets['notes']))
		db.cnx.commit()

db = sqlHandler.DbInterface(dbConfig.db)
fiets = jsonHandler.deserializeJson()
response = {"errorCode": newFiets(fiets)}
jsonHandler.serializeJson(response)
db.close()
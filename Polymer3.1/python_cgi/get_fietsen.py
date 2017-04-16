#!/usr/bin/env python
from helpers import *

def getFietsen():
		db.cursor.execute("SELECT * FROM FIETSEN")
		db.cnx.commit()
		fietsen = db.cursor.fetchall()
		print(fietsen)
		return fietsen

db = sqlHandler.DbInterface(dbConfig.db)
response = {"errorCode": getFietsen()}
jsonHandler.serializeJson(response)
db.close()
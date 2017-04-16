p#!/usr/bin/env python
from helpers import *

def getFietsen():
		db.cursor.execute("SELECT * FROM FIETSEN")
		db.cnx.commit()
		fietsen = db.cursor.fetchall()
		return fietsen

db = sqlHandler.DbInterface(dbConfig.db)
jsonHandler.serializeJson(getFietsen())
db.close()
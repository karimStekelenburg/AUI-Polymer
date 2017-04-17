#!/usr/bin/env python
from helpers import *


def updateFiets(update_request):
		try:
				db.cursor.execute("""
			  UPDATE Fietsen
				SET Status=%s
				WHERE id=%s
			""", (update_request['status'], update_request['id']))
				db.cnx.commit()
				return "success"
		
		except:
				return "sql error"


db = sqlHandler.DbInterface(dbConfig.db)
update_request = jsonHandler.deserializeJson()
response = {"errorCode": updateFiets(update_request)}
jsonHandler.serializeJson(response)
db.close()

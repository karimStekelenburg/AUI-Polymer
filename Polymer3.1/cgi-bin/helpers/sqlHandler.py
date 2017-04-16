#!/usr/bin/env python
import mysql.connector


class DbInterface(object):
    def __init__(self, configDict):
        config = configDict

        mysql.connector.paramstyle = 'format'

        try:
            self.cnx = mysql.connector.connect(**config)  # connect to db using the config.py file
            self.cursor = self.cnx.cursor(buffered=True,
                                          dictionary=True)  # handler structure for inserting datat into the db

        except:
            print("ERROR: failed to connect to the database,'\ncheck configs")

    def close(self):
        self.cnx.close()
        self.cursor.close()

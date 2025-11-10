from errno import errorcode

import mysql
from mysql.connector import cursor

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""


class MuseoDAO:
    def __init__(self):
        pass

    def get_all_musei(self):

        query = """
            SELECT nome
            FROM museo
        """

        cnx = ConnessioneDB().get_connection()
        if cnx is None:
            return None

        try:
            cursor = cnx.cursor()
            cursor.execute(query)

            risultato = cursor.fetchall()
            cursor.close()
            cnx.close()

            if not risultato:
                return None

            musei = []
            for row in risultato:
                musei.append(row[0])
            return musei

        except mysql.connector.Error as err:
            print("Something is wrong with your user name or password")
            return None
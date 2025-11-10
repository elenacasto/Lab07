import mysql

from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def get_artefatti_filtrati(self, museo:str, epoca:str):

        query = """
            SELECT *
            FROM artifatti
            WHERE 1=1
        """
        parametri = []

        if museo:
            query += "AND museo = ?"
            parametri.append(museo)
        if epoca:
            query += "AND epoca = ?"
            parametri.append(epoca)

        cnx = ConnessioneDB().get_connection()
        if cnx is None:
            return None

        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, parametri)

            risultato = cursor.fetchall()
            cursor.close()
            cnx.close()

            if not risultato:
                return None

            artefatti = []
            for row in risultato:
                artefatti.append(Artefatto(**row))
            return artefatti

        except mysql.connector.Error as err:
            print("Errore nella query: {}".format(err))
            return None

    def get_epoche(self):

        query = """
            SELECT DISTINCT epoca 
            FROM artefatti
            ORDER BY epoca
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

            epoca = []
            for row in risultato:
                epoca.append(row[2])
            return epoca

        except mysql.connector.Error as err:
            print("Something is wrong with your user name or password")
            return None
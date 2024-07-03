from database.DB_connect import DBConnect
from model.airport import Airport
from model.Connessione import Connessione


class DAO():

    @staticmethod
    def getAllNodes(numcomp, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT tmp.ID,tmp.IATA_CODE,COUNT(*)as N
                    FROM (SELECT a.ID ,a.IATA_CODE ,f.AIRLINE_ID ,COUNT(*) as n 
                    FROM airports a,flights f 
                    WHERE a.ID =f.ORIGIN_AIRPORT_ID or a.ID =f.DESTINATION_AIRPORT_ID 
                    GROUP BY a.ID ,a.IATA_CODE ,f.AIRLINE_ID ) as tmp
                    GROUP BY tmp.ID,tmp.IATA_CODE
                    HAVING N >= %s"""

        cursor.execute(query, (numcomp,))

        for row in cursor:
            result.append(idMap[row["ID"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.ORIGIN_AIRPORT_ID ,f.DESTINATION_AIRPORT_ID,COUNT(*) as n
                    FROM flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID ,f.DESTINATION_AIRPORT_ID
                    ORDER BY f.ORIGIN_AIRPORT_ID ,f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row["ORIGIN_AIRPORT_ID"]],
                                      idMap[row["DESTINATION_AIRPORT_ID"]],
                                      row["n"]))

        cursor.close()
        conn.close()
        return result

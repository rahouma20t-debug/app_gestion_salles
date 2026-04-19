import mysql.connector
import json

class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (salle.code, salle.description, salle.categorie, salle.capacite))

        conn.commit()
        conn.close()
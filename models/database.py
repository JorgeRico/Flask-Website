import mysql.connector
from dotenv import load_dotenv
import os

class Database():
    def __init__(self):
        load_dotenv()
        self.db_config = {
            'host'     : os.getenv('MYSQL_HOST'),
            'user'     : os.getenv('MYSQL_USER'),
            'password' : os.getenv('MYSQL_PASSWORD'),
            'database' : os.getenv('MYSQL_DB')
        }

    def connect(self):
        conn = mysql.connector.connect(**self.db_config)

        return conn

    def getJsonData(self, query):
        try:
            conn   = self.connect()
            cursor = conn.cursor()
            result = cursor.execute(query)
            # json array
            rows = [x for x in cursor]
            cols = [x[0] for x in cursor.description]
            result = []
            for row in rows:
                res = {}
                for prop, val in zip(cols, row):
                    res[prop] = val
                result.append(res)
            
            return result
        except mysql.connector.Error as err:
            # return jsonify({'error': str(err)})
            return err
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def updateData(self, query):
        try:
            conn   = self.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except mysql.connector.Error as err:
            # return jsonify({'error': str(err)})
            return err
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def insertData(self, query):
        try:
            conn   = self.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            # res = 

            # print(res)
            return cursor.lastrowid
        except mysql.connector.Error as err:
            # return jsonify({'error': str(err)})
            return err
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()
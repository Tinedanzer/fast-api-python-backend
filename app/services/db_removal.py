import sqlite3
from typing import List
from app.services.db_connection import get_connection

def del_traveler(tablename:str):
    sql= 'DELETE FROM {tablename} WHERE id = "11133";'
    # fieldnames = data[0].keys()
    sql=sql.format(
        tablename=tablename
        )
    con= get_connection()
    cursor= con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()
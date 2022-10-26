import sqlite3
from typing import List
from app.services.db_connection import get_connection
# mogrifier lookup
# make comments through this JOHN
def table_insertion(tablename:str, data: List[dict]):
    sql= 'INSERT INTO {tablename} ({fieldnames}) values {values};'
    fieldnames = data[0].keys()
# list comprehension
    lists_of_values = [record.values() for record in data]
    formattedsql = sql.format(
        tablename=tablename, 
        fieldnames= ", ".join(fieldnames),
        values = ", ".join(
            [
                "({valuelist})".format(
                    # using "?" here to help prevent sql injection into the :value
                    valuelist=",".join(["?" for _ in records])
                )
                for records in lists_of_values
            ]
        )
        # ", ".join(["({valuelist})".format(valuelist=records) for records in value])
    )
    paramaterized_list = []
    for lists in lists_of_values:
        for value in lists:
            paramaterized_list.append(value)
    # the below is the same as the above, below is AK
# data: List[dict] = []
# one_dimensional_list = [
#     v
#     for rec in data
#     for v in rec.values()
# ]
    print(formattedsql)
    print(paramaterized_list)
    con= get_connection() 
    cursor= con.cursor()
    cursor.execute(formattedsql, paramaterized_list)
    con.commit()
    con.close()
# 2,'Andrew','ail@email.com','123 sad street', "20221006"

# insert into table_name (`field_1`, `field_2`)
# values (1, 2), (3, 4);


# from app.services.db_inserts import table_insertion
# table_insertion('Travelers', [{'id':4,'name':'AK','email':'bobby tables', 'address':'happy street', 'creation_date':'2020-05-05'}])
# from app.services.db_connection import get_travelers

# fun notes
# BITWISE OPERATORS
# these operators shift bit code
# ^ = XOR
# & = AND
# >> = shift left
# << = shift right

# x=10
# y=2

# x & y = 2
# this equals two because the only spot the numbers match up in the binary is on the 2 position. 0010
# great to check for odd/even if you're bored of modulus
import sqlite3


def get_travelers():
    con = sqlite3.connect("travelers.sqlite3")
# look up cursor JOHN
    c = con.cursor()
    c.execute('''SELECT * FROM Travelers''')
    d = c.fetchall()
    return d

def get_connection():
    return sqlite3.connect("travelers.sqlite3")














# from app.services.db_setup import (
#     Travelers, 
#     engine,
# )
# from sqlalchemy.orm import sessionmaker
# from app.services.APIendpoint import (
#     carebear_output,
# )

# Session = sessionmaker(bind=engine)
# session = Session()

# for x in carebear_output:
#     id =
#     name = 
#     email = 
#     address = 

    # update = Travelers(x, name, email, address, creation_date)
    # session.add(update)

# session.commit()
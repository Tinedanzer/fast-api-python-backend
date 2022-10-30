import sqlite3


def get_travelers():
    con = sqlite3.connect("travelers.sqlite3")
# look up cursor JOHN
    c = con.cursor()
    c.execute('''SELECT * FROM Travelers''')
    d = c.fetchall()
    return d
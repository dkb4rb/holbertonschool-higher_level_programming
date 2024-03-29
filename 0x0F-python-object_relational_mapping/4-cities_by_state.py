#!/usr/bin/python3
"""
Create ne function to conect MySQLdb
"""

import sys
import MySQLdb


def new_process():
    """ Values for the connect to the database """
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    """Stattics values to nc connection"""
    ht = "localhost"
    pt = 3306

    """Connecting to the database"""
    d_b = MySQLdb.connect(host=ht, user=usr, password=pwd, db=db, port=pt)

    """The cursor gives us the ability to have multiple seperate
    working environments through the same connection to the database"""
    cur = d_b.cursor()

    """Executing the query"""
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM `states` \
    INNER JOIN cities \
    ON states.id = cities.state_id \
    ORDER BY cities.id")

    """ Show the results find """
    [print(state) for state in cur.fetchall()]

    cur.close()

    """Closing the connection to the database"""
    d_b.close()


if __name__ == "__main__":
    new_process()

#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a connection
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2],
        database=sys.argv[3], charset="utf8")
    # Perform database operations
    cur = db.cursor()

    # Fetch results
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the connection
    cur.close()
    db.close()
